"""Reject credential-shaped values and signed URLs without printing their contents.

Checks Git-tracked files by default; optional paths additionally inspect incoming
assessment packages before integration. This is a targeted publication guard,
not a claim to detect every possible secret.
"""
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import parse_qsl, urlsplit

ROOT = Path(__file__).resolve().parents[4]
TOKEN = re.compile(
    r"(?:ASIA|AKIA)[A-Z0-9]{16}|github_pat_[A-Za-z0-9_]{30,}"
    r"|gh[pousr]_[A-Za-z0-9]{30,}|sk-proj-[A-Za-z0-9_-]{30,}"
    r"|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"
)
URL = re.compile(r"https?://[^\s\"<>]+")
SENSITIVE_QUERY_NAMES = {
    "awsaccesskeyid", "x-amz-credential", "x-amz-security-token",
    "x-amz-signature", "access_token", "api_key", "apikey",
    "client_secret", "password", "securitytoken",
}


def findings(path):
    try:
        text = path.read_text()
    except (UnicodeDecodeError, FileNotFoundError):
        return []
    found = []
    for number, line in enumerate(text.splitlines(), 1):
        if TOKEN.search(line):
            found.append((number, "credential-shaped value"))
        for match in URL.finditer(line):
            try:
                parsed = urlsplit(match.group().rstrip(").,;"))
                names = {key.lower() for key, _ in parse_qsl(parsed.query)}
                if names & SENSITIVE_QUERY_NAMES or parsed.password:
                    found.append((number, "credential-bearing URL"))
            except ValueError:
                continue
    return found


def main():
    paths = {
        ROOT / name for name in subprocess.check_output(
            ["git", "ls-files", "-z"], cwd=ROOT
        ).decode().split("\0") if name
    }
    for arg in sys.argv[1:]:
        path = Path(arg).resolve()
        paths.update(p for p in path.rglob("*") if p.is_file()) if path.is_dir() else paths.add(path)
    count = 0
    for path in sorted(paths):
        for line, kind in findings(path):
            print(f"FAIL: {path}:{line}: {kind}; value withheld")
            count += 1
    if count:
        return 1
    print(f"PASS: targeted credential/signed-URL scan of {len(paths)} files; values never displayed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
