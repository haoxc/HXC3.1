#!/usr/bin/env python3
"""Push with diagnostics and a HTTP/1.1 fallback for common GitHub transport failures."""

from __future__ import annotations

import argparse
import subprocess
import sys


TRANSIENT_TRANSPORT_PATTERNS = [
    "SSL_ERROR_SYSCALL",
    "HTTP/2 stream",
    "curl 92",
    "curl 56",
    "RPC failed",
    "early EOF",
    "the remote end hung up unexpectedly",
    "Operation timed out",
    "Could not resolve host",
]


def run_git(args: list[str], check: bool = False) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        check=check,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )


def print_result(result: subprocess.CompletedProcess[str]) -> None:
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)


def current_branch() -> str:
    result = run_git(["branch", "--show-current"])
    branch = result.stdout.strip()
    if result.returncode != 0 or not branch:
        raise RuntimeError("Cannot determine current branch.")
    return branch


def current_head() -> str:
    result = run_git(["rev-parse", "HEAD"])
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "Cannot determine HEAD.")
    return result.stdout.strip()


def upstream_ref() -> str | None:
    result = run_git(["rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}"])
    if result.returncode != 0:
        return None
    return result.stdout.strip()


def parse_remote_branch(push_args: list[str]) -> tuple[str, str]:
    remote = "origin"
    branch = current_branch()

    positional = [arg for arg in push_args if not arg.startswith("-")]
    if positional:
        remote = positional[0]
    if len(positional) >= 2:
        refspec = positional[1]
        branch = refspec.split(":", 1)[-1] if ":" in refspec else refspec
        branch = branch.removeprefix("refs/heads/")
    else:
        upstream = upstream_ref()
        if upstream and "/" in upstream:
            remote, branch = upstream.split("/", 1)

    return remote, branch


def remote_head(remote: str, branch: str) -> str | None:
    result = run_git(["ls-remote", "--heads", remote, branch])
    if result.returncode != 0:
        return None
    line = result.stdout.strip().splitlines()
    if not line:
        return None
    return line[0].split()[0]


def remote_matches_head(remote: str, branch: str) -> bool:
    try:
        return remote_head(remote, branch) == current_head()
    except RuntimeError:
        return False


def is_transport_failure(output: str) -> bool:
    return any(pattern.lower() in output.lower() for pattern in TRANSIENT_TRANSPORT_PATTERNS)


def push(push_args: list[str], force_http11: bool = False) -> subprocess.CompletedProcess[str]:
    if force_http11:
        return run_git(["-c", "http.version=HTTP/1.1", "push", *push_args])
    return run_git(["push", *push_args])


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run git push with remote verification and HTTP/1.1 fallback for GitHub transport failures."
    )
    parser.add_argument("push_args", nargs=argparse.REMAINDER, help="Arguments passed after git push.")
    parser.add_argument("--no-retry", action="store_true", help="Disable HTTP/1.1 fallback retry.")
    args = parser.parse_args()

    push_args = args.push_args
    if push_args and push_args[0] == "--":
        push_args = push_args[1:]

    remote, branch = parse_remote_branch(push_args)

    print(f"Push target: {remote}/{branch}")
    first = push(push_args)
    print_result(first)

    if first.returncode == 0:
        if remote_matches_head(remote, branch):
            print(f"OK: remote {remote}/{branch} matches local HEAD {current_head()[:7]}.")
        else:
            print("WARNING: push succeeded, but remote verification did not confirm the local HEAD.")
        return 0

    combined = f"{first.stdout}\n{first.stderr}"

    if remote_matches_head(remote, branch):
        print(f"OK: push command failed after remote update; {remote}/{branch} already matches local HEAD.")
        return 0

    if not args.no_retry and is_transport_failure(combined):
        print("Transport failure detected. Retrying with git -c http.version=HTTP/1.1 push ...")
        second = push(push_args, force_http11=True)
        print_result(second)
        if second.returncode == 0:
            if remote_matches_head(remote, branch):
                print(f"OK: remote {remote}/{branch} matches local HEAD {current_head()[:7]}.")
            else:
                print("WARNING: retry succeeded, but remote verification did not confirm the local HEAD.")
            return 0
        if remote_matches_head(remote, branch):
            print(f"OK: retry failed after remote update; {remote}/{branch} already matches local HEAD.")
            return 0
        return second.returncode

    print("Push failed and no safe fallback condition was detected.")
    print("Next checks: git status -sb; git branch -vv; git remote -v; git ls-remote --heads origin")
    return first.returncode


if __name__ == "__main__":
    raise SystemExit(main())
