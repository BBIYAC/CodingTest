# [프로그래머스] 소수 찾기
import math
from itertools import combinations

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    for num in combinations(nums, 3):
        if isPrime(sum(num)):
            answer += 1
    return answer

print(solution([1, 2, 3, 4]))