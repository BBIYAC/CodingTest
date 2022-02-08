'''
1이 될 때까지
1. N에서 1을 뺀다.
2. N을 K로 나눈다.
N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램

입력 조건
첫째 줄에 N과 K가 공백으로 구분되며 각각 자연수로 주어진다. N은 항상 K보다 크거나 같다.

출력 조건
첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값을 출력한다.

입력 예시
25 5

출력 예시
2
'''
n, k = map(int, input('>> ').split(' '))

def solution(n, k):
    count = 0
    num = n
    while(True): 
        num //= k # 2번 방법
        count += 1
        if (num<k):
            if num != 1:
                count += num%k # 1번 방법
            break
    return count

print(solution(n, k))