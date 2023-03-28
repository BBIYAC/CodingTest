# [백준 14620] 꽃길

import sys
input = sys.stdin.readline

N = int(input().rstrip())
flowers = [list(map(int, input().split())) for _ in range(N)]
min_cost = 1e9
visited = set()
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

def dfs(count, cost, v):
    global min_cost
    if count == 3:
        min_cost = min(min_cost, cost)
    else:
        for i in range(1, N-1):
            for j in range(1, N-1):
                temp_visit = set()
                temp_visit.add((i, j))
                visit = 1
                temp = flowers[i][j]
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if (nx, ny) not in v:
                            temp += flowers[nx][ny]
                            temp_visit.add((nx, ny))
                        else:
                            visit = 0
                            break
                    else:
                        visit = 0
                        break
                if visit and temp_visit:
                    v.update(temp_visit)
                    dfs(count+1, cost+temp, v)
                    v -= temp_visit 

dfs(0, 0, visited)
print(min_cost)