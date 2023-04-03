# [백준 15663] N과 M 9

from itertools import permutations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_arr = map(int, input().split())

# 순열
for perm in sorted(set(permutations(N_arr, M))):
    print(*perm)