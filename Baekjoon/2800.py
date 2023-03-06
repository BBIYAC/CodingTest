# [백준 2800] 괄호 제거

from itertools import combinations
import sys
input = sys.stdin.readline

string = input().rstrip()
stack = []
index = []
results = set()

# 좌우 괄호 인덱스 구하기
for idx, char in enumerate(string):
  if char == '(':
      stack.append(idx)
  elif char == ')':
      index.append((stack.pop(), idx))

# 인덱스 조합 구하기
for i in range(1, len(index)+1):
    for comb in combinations(index, i):
        temp = string
        for l_idx, r_idx in comb:
            temp = temp[:l_idx]+' '+temp[l_idx+1:r_idx]+' '+temp[r_idx+1:]
        results.add(temp.replace(' ', ''))

# 사전 순으로 정렬 후 출력
for result in sorted(results):
    print(result)