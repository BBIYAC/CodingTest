'''
전보
도시 C에서 출발하여 각 도시 사이에 설치된 통로를 거쳐, 최대한 많이 퍼져나갈 것이다.
각 도시의 번호와 통로가 설치되어 있는 정보가 주어졌을 때, 도시 C에서 보낸 메시지를 받게되는
도시의 총 개수와 도시들이 모두 메시지를 받는 데까지 걸리는 시간을 계산하는 프로그램

# 입력 조건
1. 첫째 줄에 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C가 주어진다.
2. 둘째 줄부터 M+1번째 줄에 걸쳐서 통로에 대한 정보 X, Y, Z가 주어지고,
이는 특정 도시 X에서 다른 특정 도시 Y로 이어지는 통로가 있으며, 메시지가 전달되는 시간이 Z라는 의미.

# 출력 조건
도시 C에서 보낸 메시지를 받는 도시의 총 개수와 총 걸리는 시간을 공백으로 구분하여 출력

# 입력 예시
3 2 1
1 2 4
1 3 2

# 출력 예시
2 4
'''
import heapq

# 도시의 개수 n, 통로의 개수 m, 메시지를 보내고자 하는 도시 c
n, m, c = map(int, input('>> ').split())
# 2차원 배열 빈 테이블로 초기화
graph = [[] for _ in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
INF = int(1e9)
distance = [INF]*(n+1)
# 통로에 대한 정보 x, y, z
for _ in range(m):
    x, y, z = map(int, input('>> ').split())
    # x번 노드에서 y번 노드로 가는 비용이 z
    graph[x].append((y, z))

# dijkstra 다익스트라 풀이법
def solution():
    # 빈 큐 생성
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하며, 큐에 삽입
    heapq.heappush(q, (0, c))
    distance[c] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드 확인
        for i in graph[now]:
            cost = dist+i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    # 도달할 수 있는 노드(도시) 개수
    count = 0
    # 도달할 수 있는 노드 중, 가장 멀리 있는 노드와의 최단 거리
    max_distance = 0
    for d in distance:
        # 도달할 수 있는 노드인 경우
        if d != INF:
            count += 1
            max_distance = max(max_distance, d)
    return str(count-1)+' '+str(max_distance)

print(solution())