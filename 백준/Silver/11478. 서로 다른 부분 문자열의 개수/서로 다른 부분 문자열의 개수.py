S = input()
ans = set()
for length in range(1, len(S) + 1):
    for index in range(len(S)):
        if index == len(S) - length + 1:
            break
        ans.add(S[index : index + length])
print(len(ans))
