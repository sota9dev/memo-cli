import json
import os
import sys

def load_memos():
    if not os.path.exists("memos.json"):
        return []
    with open("memos.json", "r", encoding="utf-8") as f:
        return json.load(f)

def save_memos(memos):
    with open("memos.json", "w", encoding="utf-8") as f:
        json.dump(memos, f, ensure_ascii=False, indent=2)

args = sys.argv
if len(args) < 2:
    print("Usage: python main.py [add/list] [text]")
    exit()
command = args[1]
memo = " ".join(args[2:]) if len(args) > 2 else ""
if command == "add":
    if memo == "":
        print("Please provide a memo to add.")
        exit()
    
    memos = load_memos()
    memos.append({"text": memo})
    save_memos(memos)
    print("Added:", memo)
elif command == "list":
    memos = load_memos()
    if not memos:
        print("No memos yet.")
    else:
        for i, memo in enumerate(memos, start=1):
            print(f"{i}. {memo['text']}")
elif command == "remove":
    if len(args) < 3:
        print("Please provide index to remove.")
        exit()
    try:
        index = int(args[2]) - 1
    except ValueError:
        print("Please provide a valid number.")
        exit()
    
    memos = load_memos()

    if index < 0 or index >= len(memos):
        print("Invalid index")
        exit()
    
    removed = memos.pop(index)
    save_memos(memos)

    print("Removed:", removed["text"])
else:
    print("Invalid command. Use 'add' to add a memo, 'list' to list memos, or 'remove' to remove a memo.")