# 팩토리얼
'''
문제
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.

출력
첫째 줄에 N!을 출력한다.
'''
import sys
# 팩토리얼 - 재귀함수
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
# 정수 N
n = int(sys.stdin.readline().rstrip())
print(fact(n))