# [프로그래머스] 제곱수 판별하기
import math
def solution(n):
    return 1 if math.sqrt(n) == int(math.sqrt(n)) else 2