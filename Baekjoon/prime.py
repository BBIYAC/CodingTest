# 소수
'''
문제
자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.
예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 
이들 소수의 합은 620이고, 최솟값은 61이 된다.

입력
입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.
M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.

출력
M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다. 
단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.

예제 입력 1
60
100

예제 출력 1
620
61

예제 입력 2
64
65

예제 출력 2
-1
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
# 자연수 M
m = int(input().rstrip())
# 자연수 N
n = int(input().rstrip())
# 소수 합
prime_sum = 0
# 소수 최소값
prime_min = n
for num in range(m, n+1):
    if isPrime(num):
        prime_sum += num
        prime_min = min(prime_min, num)
# 출력 값
if prime_sum == 0:
    print(-1)
else:
    print(prime_sum)
    print(prime_min)