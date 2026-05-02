#!/usr/bin/env python3
"""
sync-agent-skills.py — Sync skill specs from vault core to runtime SKILL.md files.

Architecture:
  99-设置/agent-skills/<name>/
    ├── core.md          # Invariant knowledge, with {{RUNTIME_PREPEND}} / {{RUNTIME_APPEND}} markers
    ├── manifest.yaml    # Per-runtime config: frontmatter, prepend, append blocks
    ├── hermes/SKILL.md  # Generated → sync to ~/.hermes/skills/<category>/<name>/SKILL.md
    ├── codex/SKILL.md   # Generated → sync to ~/.codex/skills/<name>/SKILL.md
    └── claude-code/     # Generated → sync to {local,global}/.claude/skills/<name>/SKILL.md

Usage:
  python3 sync-agent-skills.py [--dry] [--skill <name>] [--runtime hermes|codex|claude-code]

After vault dir changes, rerun generate_vault_index.py.
"""

import yaml
import os
import sys
import argparse
import shutil
from datetime import date

VAULT = os.path.expanduser("~/__Data/00_Knowledges/Vault_HXC3.1(Apple)")
CORE_DIR = os.path.join(VAULT, "99-设置/agent-skills")


def load_manifest(skill_name):
    path = os.path.join(CORE_DIR, skill_name, "manifest.yaml")
    with open(path) as f:
        return yaml.safe_load(f)


def load_core(skill_name):
    path = os.path.join(CORE_DIR, skill_name, "core.md")
    with open(path) as f:
        return f.read()


def build_skill(skill_name, runtime):
    """Assemble SKILL.md: frontmatter + prepend + core + append."""
    manifest = load_manifest(skill_name)
    rt = manifest.get("runtimes", {}).get(runtime, {})
    if not rt.get("enabled", True):
        print(f"  [{runtime}] disabled in manifest, skipping")
        return None

    # --- Frontmatter ---
    fm = rt.get("frontmatter", {})
    fm_lines = []
    fm_lines.append(f"name: {manifest['name']}")

    desc = fm.get("description") or manifest.get("description", "")
    fm_lines.append(f"description: {desc}")

    for key in ["triggers", "related_skills", "version"]:
        val = fm.get(key)
        if val is None:
            continue
        if isinstance(val, list):
            fm_lines.append(f"{key}:")
            for item in val:
                fm_lines.append(f'  - "{item}"')
        else:
            fm_lines.append(f"{key}: {val}")

    frontmatter = "\n".join(["---"] + fm_lines + ["---"]) + "\n"

    # --- Body ---
    core = load_core(skill_name)
    prepend = rt.get("prepend", "")
    append = rt.get("append", "")

    # Replace markers in core
    core = core.replace("{{RUNTIME_PREPEND}}", prepend.strip())
    core = core.replace("{{RUNTIME_APPEND}}", append.strip())

    # Clean up double blank lines
    body = core.strip()
    while "\n\n\n" in body:
        body = body.replace("\n\n\n", "\n\n")

    return frontmatter + "\n" + body + "\n"


def sync_skill(skill_name, runtimes=None, dry=False):
    """Sync one skill to specified runtimes (default: all enabled)."""
    manifest = load_manifest(skill_name)
    source_skill_dir = os.path.join(CORE_DIR, skill_name)
    resource_dirs = ["agents", "references", "scripts", "assets"]

    def copy_resources(destination_dir, label, dry_run=False):
        copied = []
        for resource_dir in resource_dirs:
            src = os.path.join(source_skill_dir, resource_dir)
            dst = os.path.join(destination_dir, resource_dir)
            if not os.path.isdir(src):
                if os.path.isdir(dst):
                    if dry_run:
                        print(f"       [{label}] Would prune stale {resource_dir}/ → {dst}")
                    else:
                        shutil.rmtree(dst)
                        print(f"       [{label}] Pruned stale {resource_dir}/ → {dst}")
                continue
            copied.append(resource_dir)
            if dry_run:
                file_count = sum(len(files) for _, _, files in os.walk(src))
                print(f"       [{label}] Would sync {resource_dir}/ ({file_count} files) → {dst}")
                continue
            os.makedirs(dst, exist_ok=True)
            for root, _, files in os.walk(src):
                rel = os.path.relpath(root, src)
                target_root = dst if rel == "." else os.path.join(dst, rel)
                os.makedirs(target_root, exist_ok=True)
                for file_name in files:
                    shutil.copy2(os.path.join(root, file_name), os.path.join(target_root, file_name))
        return copied

    if runtimes is None:
        runtimes = [k for k, v in manifest.get("runtimes", {}).items() if v.get("enabled", True)]

    results = {}
    for rt in runtimes:
        content = build_skill(skill_name, rt)
        if content is None:
            continue

        rt_conf = manifest["runtimes"][rt]
        target_path = os.path.expanduser(
            rt_conf["path"].replace("$VAULT", VAULT)
        )

        if dry:
            print(f"\n  [{rt}] Would write {len(content):,} bytes → {target_path}")
            preview = content.split("\n")[:3]
            print(f"       Preview: {' | '.join(preview)[:120]}")
            copy_resources(os.path.dirname(target_path), rt, dry_run=True)
        else:
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            with open(target_path, "w") as f:
                f.write(content)
            print(f"  [{rt}] Wrote {len(content):,} bytes → {target_path}")
            copied_runtime = copy_resources(os.path.dirname(target_path), rt)
            if copied_runtime:
                print(f"       Synced resources: {', '.join(copied_runtime)}")

            # Also save generated copy locally for diff tracking
            local_path = os.path.join(CORE_DIR, skill_name, rt, "SKILL.md")
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            with open(local_path, "w") as f:
                f.write(content)
            copied_local = copy_resources(os.path.dirname(local_path), f"{rt}-generated")
            if copied_local:
                print(f"       Synced generated resources: {', '.join(copied_local)}")

        results[rt] = target_path

    # Update last_sync timestamp
    if not dry and results:
        manifest["last_sync"] = date.today().isoformat()
        manifest_path = os.path.join(CORE_DIR, skill_name, "manifest.yaml")
        with open(manifest_path, "w") as f:
            yaml.dump(manifest, f, allow_unicode=True, default_flow_style=False, sort_keys=False)

    return results


def main():
    parser = argparse.ArgumentParser(description="Sync agent skill specs from vault core to runtimes")
    parser.add_argument("--dry", action="store_true", help="Preview only, no writes")
    parser.add_argument("--skill", help="Skill name (default: all in 99-设置/agent-skills/)")
    parser.add_argument("--runtime", help="Target runtime: hermes, codex, claude-code")
    parser.add_argument("--list", action="store_true", help="List managed skills and their runtimes")
    args = parser.parse_args()

    if args.list:
        for d in sorted(os.listdir(CORE_DIR)):
            full = os.path.join(CORE_DIR, d)
            if not os.path.isdir(full) or d.startswith("."):
                continue
            try:
                m = load_manifest(d)
                rts = [k for k, v in m.get("runtimes", {}).items() if v.get("enabled", True)]
                print(f"  {d}: {', '.join(rts)}  (last_sync: {m.get('last_sync', 'never')})")
            except Exception as e:
                print(f"  {d}: ERROR — {e}")
        return

    skills = [args.skill] if args.skill else sorted(
        d for d in os.listdir(CORE_DIR)
        if os.path.isdir(os.path.join(CORE_DIR, d)) and not d.startswith(".")
    )

    runtimes = [args.runtime] if args.runtime else None

    if args.dry:
        print("=== DRY RUN ===\n")

    for skill in skills:
        print(f"Syncing: {skill}")
        try:
            sync_skill(skill, runtimes=runtimes, dry=args.dry)
        except Exception as e:
            print(f"  ERROR: {e}")

    print(f"\n{'[DRY RUN] ' if args.dry else ''}Done.")


if __name__ == "__main__":
    main()
