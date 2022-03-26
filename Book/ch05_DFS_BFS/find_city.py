'''
특정 거리의 도시 찾기
1~N번까지의 도시와 M개의 단방향 도로가 존재할 때, 
특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인
모든 도시의 번호를 출력하는 프로그램

# 입력 조건
1. 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
2. M개의 줄에 걸쳐서 두 개의 자연수 A, B가 주어지며, 각 자연수는 공백으로 구분

# 출력 조건
1. X로부터 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순 출력
2. 이 때 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1 출력

# 입력 예시 1
4 4 2 1
1 2
1 3
2 3
2 4

# 출력 예시 1
4

# 입력 예시 2
4 3 2 1
1 2
1 3
1 4

# 출력 예시 2
-1

# 입력 예시 3
4 4 1 1
1 2
1 3
2 3
2 4

# 출력 예시 3
2
3
'''

# def solution():
#     answer = 0
#     # 도시 개수 N, 도로 개수 M, 최단 거리 K, 출발 도시 번호 X
#     n, m, k, x = map(int, input('>> ').split())
#     road = []
#     for _ in range(m):
#         s, e = map(int, input('>> ').split())
#         road.append((s, e))
    
#     return answer

# print(solution())

# 정답
from collections import deque

def answer_solution():
    answer = ''
    # 도시 개수 N, 도로 개수 M, 최단 거리 K, 출발 도시 번호 X
    n, m, k, x = map(int, input('>> ').split())
    road = [[] for _ in range(n+1)]
    for _ in range(m):
        s, e = map(int, input('>> ').split())
        road[s].append(e)
    # 모든 도시에 대한 최단 거리 초기화
    distance = [-1]*(n+1)
    distance[x] = 0 # 출발 도시-출발 도시 간의 거리는 0

    # 너비 우선 탐색(BFS)
    q = deque([x])
    while q:
        now = q.popleft()
        # 현재 도시에서 이동할 수 있는 모든 도시 확인
        for next in road[now]:
            # 아직 방문하지 않은 도시라면
            if distance[next] == -1:
                # 최단 거리 갱신
                distance[next] = distance[now]+1
                q.append(next)

    # 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
    check = False
    for i in range(1, n+1):
        if distance[i] == k:
            answer += str(i)+'\n'
            check = True

    # 만약 최단 거리가 K인 도시가 없다면 -1 출력
    if check == False:
        answer = -1
    return answer

print(answer_solution())