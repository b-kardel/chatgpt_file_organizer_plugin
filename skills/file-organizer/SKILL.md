---
name: file-organizer
description: Search, inventory, classify, and organize files in any local Windows folder explicitly approved by the user. Use when the user asks to find local files, clean up a directory, identify duplicates, sort downloads, or move/rename personal files.
---

# File Organizer

Treat each requested folder as a separate, temporary scope. Ask for permission to access the exact absolute path if it is not already accessible. Do not infer approval for sibling folders, parent folders, drives, or network shares.

## Search and inventory

Confirm the requested path and intended search criteria. Use `scripts/inventory.py` for a read-only inventory when useful. Exclude hidden system locations unless the user explicitly requests them. Report the proposed scope before a large recursive scan.

## Organize safely

Before every rename, move, overwrite, or deletion, present an itemized plan containing source, destination, and collision behavior. Perform changes only after the user explicitly confirms that exact plan.

- Never delete files. Prefer a user-approved `Archive` or `Review` folder.
- Never overwrite; add a suffix or ask how to resolve collisions.
- Do not follow directory symlinks/reparse points while scanning.
- Do not handle credentials, browser profiles, or operating-system directories without an explicit request and a clear warning.
- Preserve timestamps when practical and report every completed change.

Use PowerShell native commands for approved file changes. First verify the resolved source and destination are inside the user-approved scope.
