# dfs와 bfs
'''
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
4 5 1
1 2
1 3
1 4
2 4
3 4

출력
1 2 4 3
1 2 3 4
'''
from collections import deque
import sys
input = sys.stdin.readline

# 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 번호 V
N, M, V = map(int, input().split())
# 간선이 연결하는 두 정점의 번호
points = {}
for _ in range(M):
    s, e = map(int, input().split())
    if s in points:
        points[s].append(e)
    else:
        points[s] = [e]
    if e in points:
        points[e].append(s)
    else:
        points[e] = [s]
# 정렬
for point in points:
    points[point].sort()

# DFS(깊이 우선 탐색) - 스택, 재귀
visited_dfs = [False]*N
result_dfs = [V]
visited_dfs[V-1] = True

def dfs(v):
    stack = [v]
    while stack:
        c = stack.pop()
        if c not in points:
            return
        for n in points[c]:
            if visited_dfs[n-1] == False:
                visited_dfs[n-1] = True
                result_dfs.append(n)
                stack.append(n)
                dfs(n)
dfs(V)
print(*result_dfs)
    

# BFS(너비 우선 탐색) - 큐
def bfs(v):
    answer = [v]
    q = deque()
    q.append(v)
    visited_bfs = [False]*N
    visited_bfs[v-1] = True
    while q:
        c = q.popleft()
        if c not in points:
            return answer
        for n in points[c]:
            if visited_bfs[n-1] == False:
                visited_bfs[n-1] = True
                q.append(n)
                answer.append(n)
    return answer

print(*bfs(V))