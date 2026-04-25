#!/usr/bin/env bash
set -euo pipefail

report=""
summary=""
moc=""
require_summary=0
require_moc=0

usage() {
  echo "Usage: validate_survey_bundle.sh --report <report.md> [--summary <summary.md>] [--moc <moc.md>] [--require-summary] [--require-moc]" >&2
  exit 2
}

contains_link() {
  local source_file="$1"
  local target_basename="$2"

  rg -nF "[[${target_basename%.*}" -- "$source_file" >/dev/null 2>&1 || \
  rg -nF "$target_basename" -- "$source_file" >/dev/null 2>&1
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --report)
      [[ $# -ge 2 ]] || usage
      report="$2"
      shift 2
      ;;
    --summary)
      [[ $# -ge 2 ]] || usage
      summary="$2"
      shift 2
      ;;
    --moc)
      [[ $# -ge 2 ]] || usage
      moc="$2"
      shift 2
      ;;
    --require-summary)
      require_summary=1
      shift
      ;;
    --require-moc)
      require_moc=1
      shift
      ;;
    *)
      usage
      ;;
  esac
done

[[ -n "$report" ]] || usage
[[ -f "$report" ]] || { echo "FAIL: report not found: $report" >&2; exit 1; }

report_base="$(basename "$report")"
echo "OK: report exists -> $report_base"

if rg -n '^## 调研摘要$|^\> \[!abstract\] 调研摘要' -- "$report" >/dev/null 2>&1; then
  echo "OK: report contains abstract section"
else
  echo "FAIL: report does not contain an abstract section" >&2
  exit 1
fi

if [[ "$require_summary" -eq 1 && -z "$summary" ]]; then
  echo "FAIL: summary is required but --summary was not provided" >&2
  exit 1
fi

if [[ -n "$summary" ]]; then
  [[ -f "$summary" ]] || { echo "FAIL: summary not found: $summary" >&2; exit 1; }
  summary_base="$(basename "$summary")"
  echo "OK: summary exists -> $summary_base"

  contains_link "$report" "$summary_base" || {
    echo "FAIL: report does not link summary: $summary_base" >&2
    exit 1
  }
  echo "OK: report links summary"

  contains_link "$summary" "$report_base" || {
    echo "FAIL: summary does not link report: $report_base" >&2
    exit 1
  }
  echo "OK: summary links report"
fi

if [[ "$require_moc" -eq 1 && -z "$moc" ]]; then
  echo "FAIL: MOC is required but --moc was not provided" >&2
  exit 1
fi

if [[ -n "$moc" ]]; then
  [[ -f "$moc" ]] || { echo "FAIL: MOC not found: $moc" >&2; exit 1; }
  echo "OK: MOC exists -> $(basename "$moc")"

  if contains_link "$moc" "$report_base"; then
    echo "OK: MOC links report"
  elif [[ -n "${summary:-}" ]] && contains_link "$moc" "$(basename "$summary")"; then
    echo "OK: MOC links summary"
  else
    echo "FAIL: MOC links neither report nor summary" >&2
    exit 1
  fi
fi

echo "PASS: survey bundle validation completed"
