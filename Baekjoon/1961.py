# [백준 2961] 도영이가 만든 맛있는 음식

from itertools import combinations
import sys
input = sys.stdin.readline

# 재료 개수 N
N = int(input().rstrip())
# 재료
materials = [list(map(int, input().split())) for _ in range(N)]
# 신맛과 쓴맛의 차이 최솟값
min_value = 1e9

for combs in [combinations(materials, i) for i in range(1, N+1)]:
    for comb in combs:
        S_value, B_value = 1, 0 # 신맛과 쓴맛 초기화
        for S, B in comb:
            S_value *= S # 신맛은 곱
            B_value += B # 쓴맛은 합
        # 신맛과 쓴맛의 차이 갱신
        min_value = min(min_value, abs(S_value - B_value))

print(min_value)