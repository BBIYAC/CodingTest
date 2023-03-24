# [백준 16439] 치킨치킨치킨

from itertools import combinations
import sys
input = sys.stdin.readline

# 고리 회원 수 N, 치킨 종류 수 M
N, M = map(int, input().split())
like = [list(map(int, input().split())) for _ in range(N)]

max_sum = 0
for a, b, c in combinations(range(M), 3):
    temp_sum = 0
    for i in range(N):
        temp_sum += max(like[i][a], like[i][b], like[i][c])
    max_sum = max(max_sum, temp_sum)

print(max_sum)