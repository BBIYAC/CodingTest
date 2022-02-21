'''
도시 분할 계획
N개의 집과 그 집들을 연결하는 M개의 길로 이루어져 있는 마을을 두 개의 분리된 마을로 분할할 계획
마을을 분할할 때는 각 분리된 마을 안에 집들이 서로 연결되도록 하고 마을 안에는 집이 하나 이상 있어야 함.
일단 분리된 두 마을 사이에 있는 길들은 없앨 수 있고, 각 분리된 마을 안에서도 임의의 두 집 사이에 경로가 
항상 존재하게 하면서 길을 더 없앨 수 있다. 위 조건을 만족하도록 길을 없애고 나머지 길의 유지비의 합을 
최소로 하는 프로그램

# 입력 조건
1. 첫째 줄에 집의 개수N, 길의 개수 M이 주어진다.
2. 둘째 줄 부터 M줄에 걸쳐 길의 정보가 A, B, C개의 정수로 공백으로 구분되어 주어지는데
   A번 집과 B번 집을 연결하는 길의 유지비가 C

# 출력 조건
길을 없애고 남은 유지비 합의 최솟값 출력

# 입력 예시
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4

# 출력 예시
8
'''

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기(최소 신장 트리)
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b



def solution():
    # 노드의 개수와 간선(union)의 개수 입력 받기
    v, e = map(int, input('>> ').split())
    parent = [0]*(v+1) # 부모 테이블 초기화

    # 모든 간선을 담을 리스트와 최종 비용을 담을 변수
    edges = []
    result = 0

    # 부모 테이블에서, 부모를 자기 자신으로 초기화
    for i in range(1, v+1):
        parent[i] = i

    # 모든 간선에 대한 정보를 입력받기
    for _ in range(e):
        a, b, cost = map(int, input('>> ').split())
        # 비용순으로 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정
        edges.append((cost, a, b))

    # 간선을 비용순으로 정렬
    edges.sort()
    # 최소 신장 트리에 포함되는 간선 중 가장 비용이 큰 간선
    last = 0 

    # 간선을 하나씩 확인
    for edge in edges:
        cost, a, b = edge
        # 사이클이 발생하지 않는 경우에만 집합에 포함
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
            last = cost
    return result-last # 최소 신장 트리를 찾은 후 가장 큰 간선 제거

print(solution())