'''
연산자 끼워 넣기
수와 수 사이에 연산자를 하나씩 넣어 수식을 하나 만들 수 있는데 이 때 주어진 수의 순서를 바꾸면 안된다.
식의 계산은 연산자 우선순위를 무시하고 앞에서부터 진행
몫이 음수일 때는 양수로 바꾼 뒤 계산 후 음수로 바꿈

N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램

# 입력 조건
1. 수의 개수 N
2. 수 출력
3. 합이 N-1개인 4개의 정수, 차례로 덧셈(+), 뺄셈(-), 곱셈(*), 나눗셈(/)

# 출력 조건
1. 만들 수 있는 식의 결과의 최댓값 출력
2. 최솟값 출력

# 입력 예시 1
2
5 6
0 0 1 0

# 출력 예시 1
30
30

# 입력 예시 2
3
3 4 5
1 0 1 0

# 출력 예시 2
35
17

# 입력 예시 3
6
1 2 3 4 5 6
2 1 1 1

# 출력 예시 3
54
-24
'''
from itertools import permutations

def solution():
    n = int(input('>> '))
    num = list(map(int, input('>> ').split()))
    input_operator = list(map(int, input('>> ').split()))
    operator = []
    for i in range(4):
        for _ in range(input_operator[i]):
            operator.append(i)
    ops = list(permutations(operator, len(operator)))
    max_answer = -1e9
    min_answer = 1e9
    for tuple_op in ops:
        list_op = list(tuple_op)
        answer = num[0]
        for i, op in enumerate(list_op):
            if op == 0: # (+)
                answer += num[i+1]
            elif op == 1: # (-)
                answer -= num[i+1]
            elif op == 2: # (*)
                answer *= num[i+1]
            else: # (/)
                if answer < 0:
                    answer = -((-answer) // num[i+1])
                else:
                    answer //= num[i+1]
        max_answer = max(max_answer, answer)
        min_answer = min(min_answer, answer)
                
    return str(max_answer)+'\n'+str(min_answer)

print(solution())

# 정답

n = int(input('>> '))
# 연산을 수행하고자 하는 수 리스트
data = list(map(int, input('>> ').split()))
# 더하기, 빼기, 곱하기, 나누기 연산자 개수
add, sub, mul, div = map(int, input('>> ').split())

# 최솟값과 최댓값 초기화
min_value = 1e9
max_value = -1e9

# 깊이 우선 탐색(DFS) 메서드
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i+1, now+data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, now-data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, now*data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now/data[i]))
            div += 1

def answer_solution():
    dfs(1, data[0])
    return str(max_value)+'\n'+str(min_value)
    
print(answer_solution())