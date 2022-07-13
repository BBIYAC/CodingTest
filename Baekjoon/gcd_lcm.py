# 최대공약수와 최소공배수
'''
문제
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

출력
첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소공배수를 출력한다.

예제 입력 1
24 18

예제 출력 1
6
72
'''

import sys

# 두 개의 자연수
n1, n2 = map(int, sys.stdin.readline().split())
# 최대공약수
def gcd(n1, n2):
    n1, n2 = max(n1, n2), min(n1, n2)
    # 유클리드 호제법 : 반복문 사용
    while (n2 > 0):
        temp = n1 % n2
        n1 = n2
        n2 = temp
    return n1
    # 유클리드 호제법 : 재귀 함수 사용
    # if n2 == 0:
    #     return n1
    # else:
    #     return gcd(n2, n1%n2)

print(gcd(n1, n2))

# 최소공배수
def lcm(n1, n2):
  return (n1*n2) // gcd(n1, n2)
print(lcm(n1, n2))