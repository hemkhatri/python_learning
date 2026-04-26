# Counter: 8
import sys

def modify_self():
    # 1. Read its own source code
    with open(__file__, 'r') as f:
        lines = f.readlines()

    # 2. Modify the specific line (the first line in this case)
    current_line = lines[0]
    count = int(current_line.split(": ")[1])
    lines[0] = f"# Counter: {count + 1}\n"

    # 3. Write the changes back to the file
    with open(__file__, 'w') as f:
        f.writelines(lines)

    print(f"I have modified myself! New count: {count + 1}")

if __name__ == "__main__":
    modify_self()
