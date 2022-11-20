# [프로그래머스] 공 던지기
def solution(numbers, k):
    answer = 0
    idx = 0
    len_num = len(numbers)
    for _ in range(k - 1):
        idx += 2
        if idx >= len_num:
            idx = (idx % len_num)
        answer = numbers[idx]
    return answer