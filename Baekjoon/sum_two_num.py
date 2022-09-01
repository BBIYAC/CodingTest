# 두 수의 합
'''
입력
첫째 줄에 수열의 크기 n이 주어진다. 다음 줄에는 수열에 포함되는 수가 주어진다. 셋째 줄에는 x가 주어진다. (1 ≤ n ≤ 100000, 1 ≤ x ≤ 2000000)

예제 입력
9
5 12 7 10 9 1 2 3 11
13

예제 출력
3
'''
import sys
input = sys.stdin.readline

# 수열의 크기
n = int(input().rstrip())
# 수열에 포함되는 수
n_arr = sorted(list(map(int, input().split())))
# ai + aj = x 의 x
x = int(input().rstrip())
# ai + aj = x를 만족시키는 쌍 개수
count = 0
# i, j 초기화
i, j = 0, n-1

while i < j:
    n_sum = n_arr[i] + n_arr[j]
    if n_sum > x:
        j -= 1
    elif n_sum < x:
        i += 1
    else:
        count += 1
        i += 1
        j -= 1
print(count)