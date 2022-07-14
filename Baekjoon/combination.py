# 조합 0의 개수 구하기
'''
 문제
binomial(N,M)의 끝자리 0의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N, M (0 <= M <= N <= 2,000,000,000, N != 0)이 들어온다.

출력
첫째 줄에 binomial(N,M)의 끝자리 0의 개수 출력

예제 입력 1
25 12

예제 출력 1
2
'''

import sys

# 조합
def comb(n, k):
    if k==0 or k==n:
        return 1
    return comb(n-1, k) + comb(n-1, k-1)

# 정수 N, M
n, m = map(int, sys.stdin.readline().split())

# 조합
combination = str(comb(n, m))

# 0의 개수
print(len(combination) - len(combination.rstrip("0")))