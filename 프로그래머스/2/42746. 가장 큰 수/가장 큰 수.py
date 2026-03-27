def solution(numbers):
    numbers_str = list(map(str, numbers))
    numbers_str.sort(key=lambda x: x * 3, reverse=True)
    answer = "".join(numbers_str)
    return str(int(answer))