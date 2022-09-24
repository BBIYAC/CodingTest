# 수들의 합 2
'''
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 
이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
sum_A = A[0]
count = 0
i, j = 0, 1
while True:
    if sum_A > M:
        sum_A -= A[i]
        i += 1
    elif sum_A == M:
        count += 1
        sum_A -= A[i]
        i += 1
    elif sum_A < M:
        if j < N:
            sum_A += A[j]
            j += 1
        else:
            break

print(count)