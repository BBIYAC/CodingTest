# 소수 찾기
'''
문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 
다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.

예제 입력 1
4
1 3 5 7

예제 출력 1
3
'''
import sys

# 소수인지 아닌지 판별 함수
def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

input = sys.stdin.readline
# 수의 개수 N
n = int(input().rstrip())
# N개의 수
n_arr = list(map(int, input().split()))
# 소수 개수
count = 0
for num in n_arr:
    if isPrime(num):
        count += 1
print(count)
