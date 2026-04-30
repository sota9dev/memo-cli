# memo-cli

A simple command-line memo application that stores memos in a local file.

## Features
- Add memos
- List memos with created and updated timestamps
- Remove memos by index
- Edit memos by index

## Usage

### Add a memo
```bash
python main.py add "your memo"
```

Example output:
```text
Added: your memo at 2026-04-30 22:30:00
```

### List memos
```bash
python main.py list
```

Example output:
```text
1. your memo
   created: 2026-04-30 22:30:00
   updated: Not updated
```

### Remove a memo
```bash
python main.py remove 1
```

Example output:
```text
Removed: your memo
```

### Edit a memo
```bash
python main.py edit 1 "updated memo"
```

Example output:
```text
Edited: updated memo at 2026-04-30 22:35:00
```

After editing, `list` shows the updated timestamp:
```text
1. updated memo
   created: 2026-04-30 22:30:00
   updated: 2026-04-30 22:35:00
```

## Tech
- Python

## Author
sota9dev
