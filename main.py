import json
import sys
from datetime import datetime

FILE_NAME = "memos.json"


# ========= データ層 =========


def load_memos():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_memos(memos):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(memos, f, ensure_ascii=False, indent=2)


# ========= ビジネスロジック層 =========


def add_memo(text):
    memos = load_memos()
    memo = {"text": text, "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    memos.append(memo)
    save_memos(memos)
    return memo


def list_memos():
    return load_memos()


def remove_memo(index):
    memos = load_memos()

    if index < 0 or index >= len(memos):
        return None

    removed = memos.pop(index)
    save_memos(memos)
    return removed


def edit_memo(index, new_text):
    memos = load_memos()

    if index < 0 or index >= len(memos):
        return None

    memos[index]["text"] = new_text
    memos[index]["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_memos(memos)
    return memos[index]


# ========= CLI層 =========


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py [add/list/remove/edit] [args]")
        return

    command = sys.argv[1]

    if command == "add":
        text = " ".join(sys.argv[2:])
        if not text:
            print("Please provide a memo to add.")
            return
        memo = add_memo(text)
        print(f"Added: {memo['text']} at {memo['created_at']}")

    elif command == "list":
        memos = list_memos()

        if not memos:
            print("No memos yet.")
            return

        for i, memo in enumerate(memos, start=1):
            created_at = memo.get("created_at", "unknown")
            updated_at = memo.get("updated_at", "Not updated")
            print(f"{i}. {memo['text']}")
            print(f"   created: {created_at}")
            print(f"   updated: {updated_at}")

    elif command == "remove":
        if len(sys.argv) < 3:
            print("Please provide index to remove.")
            return

        try:
            index = int(sys.argv[2]) - 1
        except ValueError:
            print("Please provide a valid number.")
            return

        removed = remove_memo(index)
        if removed is None:
            print("Invalid index")
            return

        print(f"Removed: {removed['text']}")

    elif command == "edit":
        if len(sys.argv) < 4:
            print("Please provide index and new text.")
            return

        try:
            index = int(sys.argv[2]) - 1
        except ValueError:
            print("Please provide a valid number.")
            return

        new_text = " ".join(sys.argv[3:])
        if not new_text.strip():
            print("Please provide new text.")
            return
        memo = edit_memo(index, new_text)
        if memo is None:
            print("Invalid index")
            return

        print(f"Edited: {memo['text']} at {memo['updated_at']}")

    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
