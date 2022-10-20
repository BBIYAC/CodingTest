# [해커랭크] Queue Using Two Stacks
from collections import deque
import sys
input = sys.stdin.readline
N = int(input().rstrip())
queue = deque()
for _ in range(N):
    N_input = input().split()
    if N_input[0] == '1':
        queue.append(int(N_input[1]))
    elif N_input[0] == '2':
        queue.popleft()
    else:
        print(queue[0])