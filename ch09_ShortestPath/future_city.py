'''
미래 도시
1번부터 N번까지의 회사가 있고, X번 회사에 방문해 물건을 판매하고자 할 때
K번 회사에 방문한 뒤에 X번 회사를 방문하는 최소 시간을 계산하는 프로그램

# 입력 조건
1. 첫째 줄에 전체 회사의 개수 N과 경로의 개수 M이 공백으로 구분되어 차례대로 주어진다.
2. 둘째 줄부터 M+1번째 줄에는 연결된 두 회사의 번호가 공백으로 구분되어 주어진다.
3. M+1번째 줄에는 X와 K가 공백으로 구분되어 차례로 주어진다.

# 출력 조건
1. 첫째 줄에 방문 판매원 A가 K번 회사를 거쳐 X번 회사로 가는 최소 이동 시간을 출력한다.
2. 만약 X번 회사에 도달할 수 없다면 -1 출력

# 입력 예시 1
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

# 출력 예시 1
3

# 입력 예시 2
4 2
1 3
2 4
3 4

# 출력 예시 2
-1
'''

# 무한 값 설정
INF = int(1e9)
# 전체 회사 개수 n, 경로의 개수 m
n, m = map(int, input('>> ').split())
# 2차원 배열 생성 및 모든 값 무한으로 초기화(노드)
graph = [[INF]*(n) for _ in range(n)]
# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(n):
    graph[i][i] = 0

# 각 간선(연결된 두 회사의 번호)에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    a, b = map(int, input('>> ').split())
    a, b = a-1, b-1
    graph[a][b] = 1
    graph[b][a] = 1

# 최종 방문 회사 x, 중간에 방문할 회사 k 번호
x, k = map(int, input('>> ').split())
x, k = x-1, k-1

def solution():
    # 플로이드 워셜 알고리즘
    for k in range(n): # 거쳐가는 노드 k
        for a in range(n): # 시작 노드 a
            for b in range(n): # 도착 노드 b
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
            print(graph[a])
        print()
    # 수행된 결과
    distance = graph[0][k] + graph[k][x]
    # 도달할 수 없는 경우 -1
    if distance >= INF:
        distance = -1
    return distance

print(solution())