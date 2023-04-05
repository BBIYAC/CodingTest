# [백준 15665] N과 M 11

from itertools import product
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_arr = sorted(map(int, input().split()))

for prod in sorted(set(product(N_arr, repeat=M))):
    print(*prod)