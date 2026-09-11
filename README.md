# File Organizer plugin for Codex

This plugin helps Codex search and safely organize files in local Windows folders that the user explicitly approves.

## Safety model

- Each requested absolute folder path is a separate scope.
- Searches are read-only by default.
- Move, rename, overwrite, and delete operations require an itemized plan and explicit confirmation.
- Deletion and overwriting are disabled by default; prefer an approved Archive or Review folder.
- Symlinked directories are not followed during inventory.

The plugin includes a read-only inventory script at `scripts/inventory.py`.
