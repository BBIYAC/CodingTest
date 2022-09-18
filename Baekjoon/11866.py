# 요세푸스 순열
from collections import deque
import sys
N, K = map(int, sys.stdin.readline().split())

queue = deque(map(str, range(1, N+1)))

print('<', end='')
while queue:
    for i in range(K-1):
        num = queue.popleft()
        queue.append(num)
    out = queue.popleft()
    if len(queue) == 0:
        print(out, end='>')
    else:
        print(out, end=', ')
