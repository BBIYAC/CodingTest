# [프로그래머스] 괄호 회전하기
from collections import deque

def isCorrect(s):
    stack = [s[0]]
    for char in s[1:]:
        if not stack:
            stack.append(char)
            continue

        if ((stack[-1] == '[' and char == ']') 
            or (stack[-1] == '(' and char == ')')
            or (stack[-1] == '{' and char == '}')):
            stack.pop()
        else:
            stack.append(char)
    return False if stack else True
            
def solution(s):
    queue = deque(s)
    answer = 0
    for _ in range(len(s)):
        if isCorrect(list(queue)):
            answer += 1
        queue.append(queue.popleft())
        
    return answer

print(solution("[)(]"))