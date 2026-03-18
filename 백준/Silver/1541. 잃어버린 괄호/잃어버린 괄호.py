ans = input()


def sum_str(str):
    return sum(map(int, str.split("+")))


if ans[0] == "-":
    ans = ans[1:]
    temp = ans.split("-")
    temp_sum = [sum_str(text) for text in temp]
    print(-sum(temp_sum))
else:
    temp = ans.split("-")
    temp_sum = [sum_str(text) for text in temp]
    print(-sum(temp_sum) + temp_sum[0] * 2)
