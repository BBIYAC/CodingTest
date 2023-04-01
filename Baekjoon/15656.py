# [백준 15656] N과 M 7

from itertools import product
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_arr = sorted(list(map(int, input().split())))

for prod in product(N_arr, repeat=M):
    print(*prod)