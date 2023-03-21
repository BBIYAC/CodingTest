# [백준 5585] 거스름돈

import sys
input = sys.stdin.readline

price = 1000 - int(input().rstrip())
count = 0

for coin in [500, 100, 50, 10, 5, 1]:
    count += price // coin
    price %= coin

print(count)