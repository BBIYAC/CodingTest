# [백준 5568] 카드 놓기

from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input().rstrip())
K = int(input().rstrip())
cards = [input().rstrip() for _ in range(N)]
answer = set() # 중복 숫자 제거
for perm in permutations(cards, K):
    answer.add(''.join(perm)) # 하나의 숫자로 만든 후 추가

print(len(answer))