# [프로그래머스] 주사위 개수
def solution(box, n):
    answer = 1
    for length in box:
        answer *= length // n
    return answer