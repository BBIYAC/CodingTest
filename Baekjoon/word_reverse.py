# 단어 뒤집기
import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    words = input().split()
    for word in words:
        print(''.join(reversed(list(word))), end=' ')
    print()
