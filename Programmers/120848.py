# [프로그래머스] 팩토리얼
def solution(n):
    result = 1
    i = 1
    while True:
        result *= i
        if result > n:
            break
        i += 1
    return i - 1