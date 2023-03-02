# [백준 10866] 덱

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
queue = deque()

for _ in range(N):
  command = list(input().split())

  if command[0] == 'push_front':
    queue.appendleft(command[1])
  elif command[0] == 'push_back':
    queue.append(command[1])
  elif command[0] == 'pop_front':
    print(-1 if len(queue) == 0 else queue.popleft())
  elif command[0] == 'pop_back':
    print(-1 if len(queue) == 0 else queue.pop())
  elif command[0] == 'size':
    print(len(queue))
  elif command[0] == 'empty':
    print(1 if len(queue) == 0 else 0)
  elif command[0] == 'front':
    print(-1 if len(queue) == 0 else queue[0])
  elif command[0] == 'back':
    print(-1 if len(queue) == 0 else queue[-1])