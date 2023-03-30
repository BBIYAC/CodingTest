# [백준 15654] N과 M 5

from itertools import permutations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_arr = sorted(list(map(int, input().split())))

for perm in permutations(N_arr, M):
    print(*perm)