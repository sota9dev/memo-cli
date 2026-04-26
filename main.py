import sys
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
    with open("memo.txt", "a", encoding="utf-8") as f:
        f.write(memo + "\n")
elif command == "list":
    try:     
        with open("memo.txt", "r", encoding="utf-8") as f:
            memos = f.readlines()
            for i, memo in enumerate(memos, 1):
                print(f"{i}: {memo.strip()}")
    except FileNotFoundError:
        print("No memos yet.")
elif command == "remove":
    if len(args) < 3:
        print("Please provide index to remove.")
        exit()
    try:
        index = int(args[2]) - 1
    except ValueError:
        print("Please provide a valid number.")
        exit()
    try:
        with open("memo.txt", "r", encoding="utf-8") as f:
            memos = f.readlines()

        if index < 0 or index >= len(memos):
            print("Invalid index.")
            exit()
        removed = memos.pop(index)
        with open("memo.txt", "w", encoding="utf-8") as f:
            f.writelines(memos)
        print("Removed:", removed.strip())
    except FileNotFoundError:
        print("No memos yet.")
else:
    print("Invalid command. Use 'add' to add a memo, 'list' to list memos, or 'remove' to remove a memo.")