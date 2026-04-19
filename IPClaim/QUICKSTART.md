# QUICKSTART — Maintainers: how to apply IPClaim

This quickstart is intended for repository maintainers only. The stamping process will modify the target git repository, may overwrite files, and can push commits to the remote. Run these steps only if you are authorized to change the repository.

Prerequisites
- A git repository with at least one commit in the target repo
- `git`, `openssl`, and either `curl` or `wget` available locally
- A POSIX shell (for the POSIX example) or PowerShell (for Windows example)

Manual (safe) method

1. Copy templates into the repository root (review before committing):

```bash
cp IPClaim/LICENSE-APC.md LICENSE-APC.md
cp IPClaim/VERIFY.md VERIFY.md
cp -r IPClaim/.github/workflows .github/
git add LICENSE-APC.md VERIFY.md .github/workflows/timestamp.yml
git commit -m "[APC] Add APC license templates and timestamp workflow (maintainers only)"
```

2. Edit `LICENSE-APC.md` in the repo root and fill `AUTHOR`, `TREE HASH`, and `DATE` placeholders before publishing.

3. Push when ready. The timestamp workflow will run on push and create `.timestamps/<TREE_HASH>.tsr`.

Automated (stamp.sh) method

The provided script `IPClaim/stamp.sh` automates the steps above. It prompts before overwriting files and before pushing. Example usage from the repository root:

POSIX:

```bash
./IPClaim/stamp.sh . "Your Name" apc
```

PowerShell (from repo root):

```powershell
.\IPClaim\stamp.sh . "Your Name" apc
```

Notes
- `stamp.sh` will refuse to run on a repo with zero commits.
- `stamp.sh` asks for confirmation before overwriting existing files and before pushing.
- If you prefer to inspect changes first, use the Manual method and commit/push yourself.

Verification
- After pushing, follow `VERIFY.md` to recompute the tree hash and verify the RFC 3161 token using OpenSSL.

If you want, maintainers can run `stamp.sh` in a non-pushing mode (choose not to push) then review the commit locally before pushing.
