# [백준 11725] 트리의 부모 찾기
from collections import deque
import sys
input = sys.stdin.readline

N = int(input().rstrip())
nodes = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(N-1):
    s, e = map(int, input().split())
    nodes[s].append(e)
    nodes[e].append(s)

def find_parent(root):
    q = deque(nodes[root])
    # 루트 노드의 자식의 부모는 루트
    for i in q:
        visited[i] = root
    while q:
        node = q.popleft()
        for n in nodes[node]:
            if visited[n] == 0:
                visited[n] = node
                q.append(n)

find_parent(1)
for i in range(2, N+1):
    print(visited[i])