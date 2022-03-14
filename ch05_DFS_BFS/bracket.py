'''
괄호 변환
'('와 ')'로만 이루어진 문자열 w가 "균형잡힌 괄호 문자열"이라면 다음과 같은 과정을 통해 올바른 괄호 문자열로 변환 가능
1. 입력이 빈 문자열인 경우, 빈 문자열 반환
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리. 단, u는 "균형잡힌 괄호 문자열"로 더이상 분리 X, v는 빈 문자열 X
3. 수행한 결과 문자열을 u에 이어 붙인 후 반환
    문자열 u가 "올바른 괄호 문자열"이라면 문자열 v에 대해 1단계부터 다시 수행
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정 수행
    4-1. 빈 문자열에 첫 번째 문자로 '('를 붙임
    4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙임
    4-3. ')'를 다시 붙임
    4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙임
    4-5. 생성된 문자열 반환

"균형잡힌 괄호 문자열" p가 매개변수로 주어질 때, 주어진 알고리즘을 수행해 "올바른 괄호 문자열"로 변환
만약 p가 이미 올바른 괄호 문자열이라면 그대로 return

# 입력 예시 1
(()())()

# 출력 예시 1
(()())()

# 입력 예시 2
)(

# 출력 예시 2
()

# 입력 예시 3
()))((()

# 출력 예시 3
()(())()
'''

from collections import deque

# def solution(p):
#     answer = ''
#     q = deque(p)
#     print(q)
#     # for bracket in p:
    
#     #     q.append(bracket)

#     i = 0
#     while q:
#         if q[i] == '(':

#     return answer

# print(solution('()))((()'))


# 정답

# 균형잡힌 괄호 문자열의 인덱스 반환
def balanced_index(p):
    count = 0 # 왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

# 올바른 괄호 문자열인지 판단
def check_proper(p):
    count = 0 # 왼쪽 괄호의 개수
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0: # 쌍이 맞지 않는 경우 False 반환
                return False
            count -= 1
    return True # 쌍이 맞는 경우 True 반환

def answer_solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)
    u = p[:index+1]
    v = p[index+1:]
    # 올바른 괄호 문자열이면 v에 대해 함수를 수행한 결과를 붙여 반환
    if check_proper(u):
        answer = u + answer_solution(v)
    else:
        answer = '('
        answer += answer_solution(v)
        answer += ')'
        u = list(u[1:-1]) # 첫 번째와 마지막 문자 제거
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer

print(answer_solution('()))((()'))