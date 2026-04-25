---
name: git-commit-push-checks
description: Use for Git commit and push workflows, especially when the user says c&p, commit and push, 提交并推送, 提交到 GitHub, 推送到 GitHub, or asks to prepare an Obsidian/Vault repository for GitHub. Enforces large-file checks over the commit/push file set, archives >15MB non-Markdown Obsidian attachments into 98-附件 by referenced topic, updates Obsidian links, and verifies repo state before pushing.
---

# Git Commit Push Checks

## Purpose

Use this skill for `c&p` / commit-and-push workflows.

The default goal is not just “run git commands”. The goal is:

1. keep GitHub pushes from failing on large files;
2. keep Obsidian links valid after large attachments are moved;
3. make the commit scope explicit;
4. push only after automated checks pass.

## Required Workflow

1. Check repo state:

```bash
git status -sb
git remote -v
git branch -vv
```

2. Run the attachment archive script before committing or pushing:

```bash
python3 99-设置/codex-skills/git-commit-push-checks/scripts/archive_large_obsidian_attachments.py --apply
```

If it moved files or rewrote links, review the output and include the changed Markdown/index files in the commit. The actual large files under `98-附件` are normally ignored by `.gitignore`.

3. Stage the intended scope.

4. Audit the staged set for files larger than 15MB:

```bash
python3 99-设置/codex-skills/git-commit-push-checks/scripts/git_large_file_audit.py --staged
```

If the script reports any file larger than 15MB, stop and explicitly ask the user to confirm whether those files should be committed. Do not commit them silently.

5. Before push, audit the to-be-pushed set:

```bash
python3 99-设置/codex-skills/git-commit-push-checks/scripts/git_large_file_audit.py --ahead
```

If this reports files larger than 15MB, stop and ask for user confirmation before pushing.

6. Push only after checks pass. Prefer the bundled safe push script over raw `git push`:

```bash
python3 99-设置/codex-skills/git-commit-push-checks/scripts/safe_git_push.py
```

If upstream is missing:

```bash
python3 99-设置/codex-skills/git-commit-push-checks/scripts/safe_git_push.py -- -u origin <branch>
```

## Confirmation Rule

Any file larger than 15MB in the staged set or push-ahead set requires explicit user confirmation.

Use direct wording:

```text
本次提交/推送列表中有以下超过 15MB 的文件。请确认是否继续提交/推送这些文件：
...
```

Do not treat “below GitHub 100MB” as automatic approval. The user asked for a 15MB review gate.

## Obsidian Attachment Archive Rule

Before push, always run the archive script. It scans for non-Markdown files larger than 15MB outside `98-附件`, finds Markdown notes that reference them, moves the files into `98-附件` using the referenced note/topic as the subdirectory basis, and rewrites Obsidian links.

Expected behavior:

- Markdown files are never moved by the archive script.
- Files already under `98-附件` are left in place.
- If a referenced topic cannot be inferred, the file goes under `98-附件/05-待确认附件/<source-folder-or-filename>/`.
- After moving files, rerun the script or inspect its verification output to ensure old references are gone.

## Push Failure Handling

Do not blindly retry failed pushes.

Diagnose in this order:

1. repo state: `git status -sb`, `git branch -vv`, `git remote -v`;
2. content risk: run both large-file audit modes;
3. remote state: `git ls-remote --heads origin`;
4. credentials/network/transport.

If GitHub returns a server-side error but `git ls-remote --heads origin` shows the pushed commit on the target branch, treat the push as likely successful and verify with `git status -sb`.

For HTTPS transport failures such as `LibreSSL SSL_connect: SSL_ERROR_SYSCALL`, `HTTP/2 stream`, `curl 92`, `RPC failed`, or `early EOF`, use:

```bash
python3 99-设置/codex-skills/git-commit-push-checks/scripts/safe_git_push.py
```

The script will:

1. run a normal `git push`;
2. verify whether the remote branch already reached local `HEAD`;
3. retry once with `git -c http.version=HTTP/1.1 push` for known transport failures;
4. verify remote state again before reporting success or failure.
