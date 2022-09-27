# [백준 1759] 암호 만들기
from itertools import combinations
import sys
input = sys.stdin.readline

L, C = map(int, input().split())
alphabet = sorted(input().split())

for word in combinations(alphabet, L):
    count = 0
    for w in word:
        if w in 'aeiou':
            count += 1
    if 1<= count <= L-2: 
        print(''.join(word))
