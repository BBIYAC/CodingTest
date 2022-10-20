# [해커랭크] Breadth First Search
'''
2
4 2
1 2
1 3
1
3 1
2 3
2

6 6 -1
-1 6
'''
from collections import deque
def bfs(n, m, edges, s):
    nodes = [[] for _ in range(n+1)]
    visited = [-1 for _ in range(n+1)]
    for a, b in edges:
        nodes[a].append(b)
        nodes[b].append(a)
    q = deque()
    q.append(s)
    visited[s] = 0
    while q:
        c = q.popleft()
        for node in nodes[c]:
            if visited[node] == -1:
                q.append(node)
                visited[node] = visited[c] + 1
    for i in range(1, n+1):
        if visited[i] != -1:
            visited[i] *= 6
    return visited[1:s]+visited[s+1:]

t = int(input().rstrip())

for _ in range(t):
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    s = int(input().rstrip())
    print(bfs(n, m, edges, s))