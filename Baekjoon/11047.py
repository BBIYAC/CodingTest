# [백준 11047] 동전 0
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = [int(input().rstrip()) for _ in range(N)][::-1]
coin = 0
for i in A:
    if K == 0:
        break
    if i <= K:
        coin += K//i
        K -= i * (K//i)
print(coin)