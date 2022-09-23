# [백준 9095] 1,2,3 더하기
from itertools import product
import sys
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    count = 0
    for i in range(1, N+1):
        for nums in product([1, 2, 3], repeat=i):
            sum_nums = sum(nums)
            if sum_nums == N:
                count += 1
    print(count)