# [백준 11403] 경로 찾기
import sys
input = sys.stdin.readline

N = int(input().rstrip())
graph = [list(map(int, input().split())) for _ in range(N)]
        
#플로이드-워셜 알고리즘
for k in range(N):
    for i in range(N):
        for j in range(N): # i점과 j점이 직접 연결된 경우와 i점에서 k점을 거쳐 j에 도달하는 경우
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1

for g in graph:
    print(*g)