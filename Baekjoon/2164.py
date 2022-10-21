# [백준 2164] 카드 2
from collections import deque
import sys
N = int(sys.stdin.readline().rstrip())
queue = deque(range(1, N+1))
while len(queue) > 2:
    queue.popleft()
    first = queue.popleft()
    queue.append(first)

print(queue.pop())