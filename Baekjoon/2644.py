# [백준 2644] 촌수 계산
from collections import deque
import sys
input = sys.stdin.readline

# 전체 사람 수 N
N = int(input().rstrip())
# 촌수 알고싶은 두 사람 A, B
A, B = map(int, input().split())
# 부모 자식 간의 관계 수 M
M = int(input().rstrip())
Nodes = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    # 부모 X 자식 Y
    X, Y = map(int, input().split())
    Nodes[X].append(Y)
    Nodes[Y].append(X)

def bfs(start):
    q = deque()
    q.append(start)
    while q:
        c = q.popleft()
        for n in Nodes[c]:
            if visited[n] == 0:
                visited[n] = visited[c] + 1
                q.append(n)
bfs(A)
print(visited[B] if visited[B] != 0 else -1)