#!/usr/bin/env python3
"""Archive large non-Markdown Obsidian attachments into 98-附件 and rewrite links."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


ATTACH_ROOT = "98-附件"
DEFAULT_THRESHOLD_MB = 15.0


@dataclass
class Ref:
    note: Path
    kind: str
    matched: str


@dataclass
class Plan:
    source: Path
    dest: Path
    refs: list[Ref]
    reason: str


def repo_root() -> Path:
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode == 0:
        return Path(result.stdout.decode().strip())
    return Path.cwd()


def rel_posix(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def is_markdown(path: Path) -> bool:
    return path.suffix.lower() in {".md", ".markdown"}


def should_skip(path: Path, root: Path) -> bool:
    rel = rel_posix(path, root)
    parts = path.relative_to(root).parts
    return (
        ".git" in parts
        or parts[:1] == (ATTACH_ROOT,)
        or ".obsidian" in parts
        or path.name == ".DS_Store"
        or is_markdown(path)
    )


def large_non_md_files(root: Path, threshold: int) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file() or should_skip(path, root):
            continue
        try:
            if path.stat().st_size > threshold:
                files.append(path)
        except OSError:
            continue
    return files


def markdown_notes(root: Path) -> list[Path]:
    ignored_prefixes = {".git", ".obsidian", ATTACH_ROOT}
    notes: list[Path] = []
    for path in root.rglob("*.md"):
        parts = set(path.relative_to(root).parts)
        if parts.intersection(ignored_prefixes):
            continue
        notes.append(path)
    return notes


def wiki_targets(text: str) -> list[str]:
    values: list[str] = []
    for match in re.finditer(r"!?\[\[([^\]]+)\]\]", text):
        target = match.group(1).split("|", 1)[0].split("#", 1)[0].strip()
        if target:
            values.append(target)
    return values


def markdown_targets(text: str) -> list[str]:
    values: list[str] = []
    for match in re.finditer(r"!?\[[^\]]*\]\(([^)]+)\)", text):
        target = match.group(1).split("#", 1)[0].strip()
        if target and not re.match(r"^[a-z]+://", target):
            values.append(target)
    return values


def target_matches(target: str, source: Path, root: Path) -> bool:
    source_rel = rel_posix(source, root)
    normalized = target.replace("\\", "/")
    decoded = normalized.replace("%20", " ")
    return (
        decoded == source.name
        or decoded == source_rel
        or decoded.endswith("/" + source.name)
        or decoded.endswith("/" + source_rel)
    )


def find_refs(source: Path, notes: list[Path], root: Path) -> list[Ref]:
    refs: list[Ref] = []
    for note in notes:
        try:
            text = note.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            text = note.read_text(encoding="utf-8", errors="ignore")

        for target in wiki_targets(text):
            if target_matches(target, source, root):
                refs.append(Ref(note=note, kind="wiki", matched=target))

        for target in markdown_targets(text):
            if target_matches(target, source, root):
                refs.append(Ref(note=note, kind="markdown", matched=target))

        source_rel = rel_posix(source, root)
        if source_rel in text and not any(ref.note == note and ref.matched == source_rel for ref in refs):
            refs.append(Ref(note=note, kind="plain", matched=source_rel))

    return refs


def sanitize(value: str) -> str:
    value = re.sub(r"[\\/:*?\"<>|]+", "-", value)
    value = re.sub(r"\s+", " ", value).strip()
    value = value.strip(". ")
    return value[:80] or "未命名主题"


def topic_from_refs(source: Path, refs: list[Ref], root: Path) -> str:
    if refs:
        # Prefer the note title; folder-note titles are already meaningful in this Vault.
        return sanitize(refs[0].note.stem)

    generic = {"z附件", "附件", "zattachments", "assets", "项目底稿", "临时白板"}
    stage_only = re.compile(r"^\d+[-_ ]?(需求|分析|设计|客户资料|方案规划|方案跟进|需求分析|会议纪要)$")
    rel_parts = source.relative_to(root).parts[:-1]
    for name in reversed(rel_parts):
        clean = name.strip()
        if not clean or clean.lower() in generic or stage_only.match(clean):
            continue
        return sanitize(clean)
    return sanitize(source.stem)


def category_for(source: Path, refs: list[Ref], root: Path) -> str:
    haystack = " ".join([rel_posix(source, root), *(rel_posix(ref.note, root) for ref in refs)])
    suffix = source.suffix.lower()
    audio_video = {".mp3", ".m4a", ".wav", ".aac", ".flac", ".mp4", ".mov", ".mkv", ".avi", ".gif"}

    if suffix in audio_video and any(token in haystack for token in ["项目", "会议", "客户", "ZS-", "止善", "方案"]):
        return "01-项目音视频记录"
    if any(token in haystack for token in ["数字孪生案例", "案例库", "艺术", "杭州亚运会", "江苏移动", "园区"]):
        return "03-数字孪生案例库"
    if any(token in haystack for token in ["课程", "教学", "学习", "数学", "精益", "常工院"]):
        return "04-学习与课程材料"
    if any(token in haystack for token in ["项目", "方案", "需求", "客户", "ZS-", "止善", "平台规划"]):
        return "02-项目方案与需求材料"
    return "05-待确认附件"


def existing_topic_dir(root: Path, category: str, topic: str) -> Path | None:
    base = root / ATTACH_ROOT / category
    if not base.exists():
        return None
    normalized_topic = topic.lower()
    for child in base.iterdir():
        if not child.is_dir():
            continue
        name = child.name.lower()
        if name == normalized_topic or normalized_topic in name or name in normalized_topic:
            return child
    return None


def unique_dest(path: Path) -> Path:
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    i = 2
    while True:
        candidate = parent / f"{stem}-{i}{suffix}"
        if not candidate.exists():
            return candidate
        i += 1


def plan_for(source: Path, refs: list[Ref], root: Path) -> Plan:
    topic = topic_from_refs(source, refs, root)
    category = category_for(source, refs, root)
    target_dir = existing_topic_dir(root, category, topic) or (root / ATTACH_ROOT / category / topic)
    dest = unique_dest(target_dir / source.name)
    reason = "referenced topic" if refs else "source folder fallback"
    return Plan(source=source, dest=dest, refs=refs, reason=reason)


def replace_links(text: str, source: Path, dest: Path, root: Path) -> tuple[str, int]:
    old_rel = rel_posix(source, root)
    new_rel = rel_posix(dest, root)
    basename = source.name
    count = 0

    def replace_wiki(match: re.Match[str]) -> str:
        nonlocal count
        bang = "!" if match.group(0).startswith("!") else ""
        body = match.group(1)
        target, rest = split_obsidian_suffix(body)
        if target_matches(target, source, root):
            count += 1
            return f"{bang}[[{new_rel}{rest}]]"
        return match.group(0)

    def replace_md(match: re.Match[str]) -> str:
        nonlocal count
        label = match.group(1)
        target = match.group(2)
        clean = target.split("#", 1)[0]
        suffix = target[len(clean):]
        if target_matches(clean, source, root):
            count += 1
            return f"[{label}]({new_rel}{suffix})"
        return match.group(0)

    text = re.sub(r"!?\[\[([^\]]+)\]\]", replace_wiki, text)
    text = re.sub(r"\[([^\]]*)\]\(([^)]+)\)", replace_md, text)
    if old_rel in text:
        text = text.replace(old_rel, new_rel)
        count += 1
    if basename in text and old_rel != basename:
        # Only plain filename replacement remains here; wiki/markdown links were already handled.
        plain_pattern = re.compile(rf"(?<![/\w.-]){re.escape(basename)}(?![\w.-])")
        text, extra = plain_pattern.subn(new_rel, text)
        count += extra
    return text, count


def split_obsidian_suffix(body: str) -> tuple[str, str]:
    for sep in ("|", "#"):
        if sep in body:
            target, rest = body.split(sep, 1)
            return target.strip(), sep + rest
    return body.strip(), ""


def apply_plan(plan: Plan, root: Path) -> tuple[int, list[Path]]:
    plan.dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(plan.source), str(plan.dest))

    changed_notes: list[Path] = []
    total_replacements = 0
    for ref in sorted({ref.note for ref in plan.refs}):
        text = ref.read_text(encoding="utf-8", errors="ignore")
        new_text, count = replace_links(text, plan.source, plan.dest, root)
        if count and new_text != text:
            ref.write_text(new_text, encoding="utf-8")
            changed_notes.append(ref)
            total_replacements += count
    return total_replacements, changed_notes


def verify(root: Path, plans: list[Plan]) -> list[str]:
    errors: list[str] = []
    notes = markdown_notes(root)
    note_texts: list[tuple[Path, str]] = []
    for note in notes:
        note_texts.append((note, note.read_text(encoding="utf-8", errors="ignore")))

    for plan in plans:
        if not plan.dest.exists():
            errors.append(f"missing destination: {rel_posix(plan.dest, root)}")
        old_rel = rel_posix(plan.source, root)
        for note, text in note_texts:
            if old_rel in text:
                errors.append(f"old path still referenced in {rel_posix(note, root)}: {old_rel}")
    return errors


def update_index(root: Path) -> None:
    index = root / ATTACH_ROOT / f"{ATTACH_ROOT}.md"
    if not index.exists():
        return
    categories = []
    for category in sorted((root / ATTACH_ROOT).glob("*")):
        if category.is_dir():
            count = sum(1 for item in category.rglob("*") if item.is_file())
            categories.append((category.name, count))

    lines = [
        "\n## 当前目录统计\n",
        "",
        "| 子目录 | 文件数 |",
        "|---|---:|",
    ]
    for name, count in categories:
        lines.append(f"| `{name}` | {count} |")

    text = index.read_text(encoding="utf-8", errors="ignore")
    marker = "\n## 当前目录统计\n"
    if marker in text:
        text = text.split(marker, 1)[0].rstrip() + "\n" + "\n".join(lines) + "\n"
    else:
        text = text.rstrip() + "\n" + "\n".join(lines) + "\n"
    index.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Archive large non-Markdown Obsidian attachments into 98-附件.")
    parser.add_argument("--threshold-mb", type=float, default=DEFAULT_THRESHOLD_MB)
    parser.add_argument("--apply", action="store_true", help="Move files and rewrite links. Without this, only print the plan.")
    args = parser.parse_args()

    root = repo_root()
    threshold = int(args.threshold_mb * 1024 * 1024)
    notes = markdown_notes(root)
    candidates = large_non_md_files(root, threshold)

    plans = [plan_for(source, find_refs(source, notes, root), root) for source in candidates]
    if not plans:
        print(f"OK: no non-Markdown files outside {ATTACH_ROOT} larger than {args.threshold_mb:g}MB.")
        return 0

    print(f"Found {len(plans)} non-Markdown file(s) larger than {args.threshold_mb:g}MB outside {ATTACH_ROOT}:")
    for plan in plans:
        refs = ", ".join(rel_posix(ref.note, root) for ref in plan.refs[:3]) or "no markdown reference found"
        print(f"- {rel_posix(plan.source, root)} -> {rel_posix(plan.dest, root)} [{plan.reason}; refs: {refs}]")

    if not args.apply:
        print("Dry run only. Re-run with --apply to move files and rewrite links.")
        return 1

    applied: list[Plan] = []
    for plan in plans:
        replacements, changed_notes = apply_plan(plan, root)
        applied.append(plan)
        print(f"Moved: {rel_posix(plan.dest, root)}; link replacements: {replacements}; changed notes: {len(changed_notes)}")

    update_index(root)
    errors = verify(root, applied)
    if errors:
        print("Verification failed:")
        for error in errors:
            print(f"- {error}")
        return 2

    print("OK: archive complete and moved-link verification passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
