# [프로그래머스] 올바른 괄호
def solution(s):
    stack = []
    for word in list(s):
        if word == '(':
            stack.append('(')
        elif word == ')' and not stack:
            return False
        else:
            stack.pop()

    return True if not stack else False