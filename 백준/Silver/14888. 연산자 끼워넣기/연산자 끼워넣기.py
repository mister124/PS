import sys
input = sys.stdin.readline

N = int(input())
arr_a = list(map(int, input().split()))
arr_cnt = list(map(int, input().split()))
arr_op = ["+", "-", "*", "//"]
op_cnt = {op: cnt for op, cnt in zip(arr_op, arr_cnt)}

stack_op = []
total = set()

def backtrack():
    if len(stack_op) == N - 1:
        num = arr_a[0]
        for i, op in enumerate(stack_op):
            b = arr_a[i + 1]
            if op == "+": num += b
            elif op == "-": num -= b
            elif op == "*": num *= b
            elif op == "//":
                num = -(-num // b) if num < 0 else num // b
        total.add(num)
        return
    for op in op_cnt:
        if op_cnt[op]:
            stack_op.append(op)
            op_cnt[op] -= 1
            backtrack()
            stack_op.pop()
            op_cnt[op] += 1

backtrack()
print(max(total))
print(min(total))