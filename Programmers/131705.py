# [프로그래머스] 삼총사
from itertools import combinations

def solution(number):
    answer = 0
    for three in combinations(number, 3):
        if sum(three) == 0:
            answer += 1
    return answer

print(solution([-2, 3, 0, 2, -5])) # 2