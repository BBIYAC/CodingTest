# 수 정렬하기 3
'''
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 수 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''

import sys
input = sys.stdin.readline

# 수의 개수 N
n = int(input().rstrip())
# N 요소 카운트
n_arr = dict()
for _ in range(n):
    num = int(input().rstrip())
    n_arr[num] = n_arr[num]+1 if num in n_arr else 1
# 정렬 및 출력
for num in sorted(n_arr):
    for _ in range(n_arr[num]):
        print(num)