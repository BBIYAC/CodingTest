# 일곱 난쟁이
import sys
from itertools import combinations
arr = [int(sys.stdin.readline().rstrip()) for _ in range(9)]

for dwarfs in combinations(arr, 7):
    if sum(dwarfs) == 100:
        for d in sorted(dwarfs):
            print(d)
        break