from itertools import permutations
def solution(numbers):
    num_set = set()
    for i in range(1, len(numbers) + 1):
        for p in permutations(numbers, i):
            num_set.add(int("".join(p)))
    answer = 0
    for num in num_set:
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break 
        if is_prime:
            answer += 1
    return answer