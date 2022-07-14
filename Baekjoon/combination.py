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

# factorial에서 5 or 2의 개수(지수 구하기)
def factorial_5or2(n, t):
    count = 0
    while n>0:
        count += n//t
        n //= t
    return count

# 정수 N, M
n, m = map(int, sys.stdin.readline().split())

# 지수 법칙 이용 : N!에서 5 or 2의 개수 - (M!에서 5 or 2의 개수 + (N-M)!에서 5 or 2의 개수)
cnt_5=factorial_5or2(n,5)-(factorial_5or2(m,5)+factorial_5or2(n-m,5))
cnt_2=factorial_5or2(n,2)-(factorial_5or2(m,2)+factorial_5or2(n-m,2))

# 10이 되려면 5와 2 모두 있어야 하므로 5와 2 중 최솟값의 개수만큼 0의 개수가 출력됨
result=min(cnt_5,cnt_2)
print(result)