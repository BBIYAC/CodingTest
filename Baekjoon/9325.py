# [백준 9325] 얼마?
import sys
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    result = int(input().rstrip())
    N = int(input().rstrip())
    for _ in range(N):
        amount, price = map(int, input().split())
        result += amount * price
    print(result)