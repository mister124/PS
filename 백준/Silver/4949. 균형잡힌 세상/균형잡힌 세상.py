import sys

for line in sys.stdin:
    if line.rstrip("\n") == ".":
        break
    stack = []
    is_balanced = True  # 균형 여부를 체크할 플래그
    for char in line:
        if char == "(" or char == "[":
            stack.append(char)
        elif char == ")":
            if not stack or stack[-1] != "(":
                is_balanced = False
                break
            stack.pop()
        elif char == "]":
            if not stack or stack[-1] != "[":
                is_balanced = False
                break
            stack.pop()
    if is_balanced and not stack:
        print("yes")
    else:
        print("no")
