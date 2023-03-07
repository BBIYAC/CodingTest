# [백준 2493] 탑

import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().split()))
stack = []
answer = [0] * N

for i in range(N):
    tower = arr[i]
    while stack and arr[stack[-1]] < tower:
        stack.pop()
    if stack:
        answer[i] = stack[-1] + 1
    stack.append(i)
            
print(*answer)