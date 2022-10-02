# [백준 9084] 동전
import sys
input = sys.stdin.readline

# 테스트 케이스 T
T = int(input().rstrip())
for _ in range(T):
    # 동전의 가지수 N
    N = int(input().rstrip())
    # N가지 동전의 각 금액
    coins = list(map(int, input().split()))
    # 주어진 N가지 동전으로 만들 금액 M
    M = int(input().rstrip())
    # 경우의 수 
    DP = [0]*(M+1)
    DP[0] = 1
    for i in range(N):
        for j in range(coins[i], M+1):
            DP[j] += DP[j - coins[i]]

    print(DP[M])