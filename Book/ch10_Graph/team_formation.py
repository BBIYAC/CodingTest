'''
팀 결성
0번부터 N번까지의 학생들이 있고, 모든 학생이 서로 다른 팀으로 구분되어
총 N+1개의 팀이 존재한다.
1. '팀 합치기' 연산은 두 팀을 합치는 연산
2. '같은 팀 여부 확인' 연산은 특정한 두 학생이 같은 팀에 속하는지 확인하는 연산

M개의 연산을 수행할 때 '같은 팀 여부 확인' 연산에 대한 연산 결과를 출력하는 프로그램

# 입력 조건
1. 첫째 줄에 N, M이 주어진다. M은 연산의 개수
2. 다음 M개의 줄에는 각각의 연산이 주어진다.
3. '팀 합치기' 연산은 0 a b 형태(a번 학생이 속한 팀과 b번 학생이 속한 팀 합치기)
4. '같은 팀 여부 확인' 연산은 1 a b 형태(a와 b가 같은 팀에 속해 있는지 확인)
5. a와 b는 N이하의 양의 정수

# 출력 조건
'같은 팀 여부 확인' 연산에 대하여 한 줄에 하나씩 YES 혹은 NO로 결과 출력

# 입력 예시
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1

# 출력 예시
NO
NO
YES
'''

# 학생 수 n과 연산의 수 m
n, m = map(int, input('>> ').split())
# n+1개의 팀 배열
team = {}
for _ in range(n):
    team[n] = n
# m번의 연산 배열
calc = []
for _ in range(m):
    calc.append(list(map(int, input('>> ').split())))

# 딕셔너리 풀이법
def solution():
    answer = ''
    for i in range(m):
        # 두 번째 학생을 첫 번째 학생 팀에 '합치기'
        if calc[i][0] == 0: 
            team[calc[i][2]] = team.get(calc[i][1])
        # 첫 번째 학생과 두 번째 학생이 '같은 팀인지 확인'
        elif calc[i][0] == 1: # 같은 팀이면 YES
            if team.get(calc[i][1]) == team.get(calc[i][2]):
                answer += 'YES\n'
            else: # 다른 팀이면 NO
                answer += 'NO\n'
            
    return answer

print(solution())


# 서로소 집합 알고리즘 풀이법
# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

# 부모 테이블 초기화
parent = [0]*(n+1)

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(n+1):
    parent[i] = i

# 각 연산을 하나씩 확인
def set_solution():
    answer = ''
    for i in range(m):
        oper, a, b = calc[i][0], calc[i][1], calc[i][2]
        # 합집합인 경우
        if oper == 0:
            union_parent(parent, a, b)
        # 찾기인 경우
        elif oper == 1:
            if find_parent(parent, a) == find_parent(parent, b):
                answer += 'YES\n'
            else:
                answer += 'NO\n'
    return answer
print(set_solution())