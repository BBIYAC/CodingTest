'''
커리큘럼
N개의 강의를 듣고자할 때, N개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 각각 출력하는 프로그램

# 입력 조건
1. 첫째 줄에 듣고자 하는 강의의 수 N
2. 다음 N개의 줄에는 각 강의의 강의 시간과 그 강의를 듣기 위해 먼저 들어야 하는 강의들의 번호가
자연수로 주어지며, 각 자연수는 공백으로 구분
3. 각 강의 번호는 1부터 N까지로 구성되며 각 줄은 -1로 끝난다.

# 출력 조건
N개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 한 줄에 하나씩 출력

# 입력 예시
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1

# 출력 예시
10
20
14
18
17
'''
from collections import deque
import copy

# 강의 수
n = int(input('>> '))
# 모든 노드에 대한 진입 차수는 0으로 초기화
indegree = [0]*(n+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for _ in range(n+1)]
# 각 강의 시간을 0으로 초기화
time = [0]*(n+1)
# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, n+1):
    data = list(map(int, input('>> ').split()))
    time[i] = data[0] # 첫 번째 수는 시간 정보를 담고 있음
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

# 위상 정렬 함수
def topology_sort():
    answer = ''
    result = copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트
    q = deque()

    # 처음 시작할 때는 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            result[i] = max(result[i], result[now]+time[i])
            indegree[i] -= 1
            # 새롭게 진입 차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    
    # 위상 정렬을 수행한 결과 출력
    for i in range(1, n+1):
        answer += (str(result[i])+'\n')
    return answer

print(topology_sort())