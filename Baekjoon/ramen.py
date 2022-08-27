# 라면 만들기 (https://www.acmicpc.net/problem/18185)
'''
문제
라면매니아 교준이네 집 주변에는 N개의 라면 공장이 있다. 
각 공장은 1번부터 N번까지 차례대로 번호가 부여되어 있다. 
교준이는 i번 공장에서 정확하게 Ai개의 라면을 구매하고자 한다(1 ≤ i ≤ N).
교준이는 아래의 세 가지 방법으로 라면을 구매할 수 있다.

1. i번 공장에서 라면을 하나 구매한다(1 ≤ i ≤ N). 이 경우 비용은 3원이 든다.
2. i번 공장과 (i+1)번 공장에서 각각 라면을 하나씩 구매한다(1 ≤ i ≤ N-1). 이 경우 비용은 5원이 든다.
3. i번 공장과 (i+1)번 공장, (i+2)번 공장에서 각각 라면을 하나씩 구매한다(1 ≤ i ≤ N-2). 이 경우 비용은 7원이 든다.

최소의 비용으로 라면을 구매하고자 할 때, 교준이가 필요한 금액을 출력하는 프로그램을 작성하시오.

입력
첫 번째 줄에 라면 공장의 개수를 의미하는 자연수 N가 주어진다.
두번째 줄에 N개의 정수 A1, ···, AN가 사이에 공백을 두고 주어진다.

출력
첫 번째 줄에 교준이가 필요한 최소 금액을 출력한다.
'''

import sys
input = sys.stdin.readline

# 라면 공장의 개수 N
N = input()
# N개의 정수
ramens = list(map(int, input().split()))
# 최소 금액
price = 0
while sum(ramens) != 0:
    if ramens[0] == 0:
        ramens.pop(0)
        continue
    ramen_len = len(ramens)
    # i번 공장과 (i+1)번 공장, (i+2)번 공장 각각 라면을 하나씩 구매하는 경우 7원
    if ramen_len > 2 and ramens[1] != 0 and ramens[2] != 0 and ramens[1] <= ramens[2]:
        three = min(ramens[:3])
        ramens[:3] = map(lambda x: x-three, ramens[:3])
        price += 7*three
    # i번 공장과 (i+1)번 공장에서 각각 라면을 하나씩 구매하는 경우 5원
    elif ramen_len > 1 and ramens[1] != 0:
        two = min(min(ramens[:2]), ramens[1]-ramens[0])
        ramens[:2] = map(lambda x: x-1, ramens[:2])
        price += 5*two
    # i번 공장에서 라면 하나 구매하는 경우 3원
    else:
        one = ramens[0]
        ramens[0] = 0
        price += 3*one
    print(ramens, price)

print(price)