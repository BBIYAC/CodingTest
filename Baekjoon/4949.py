# [백준 4949] 균형잡힌 세상
import sys
input = sys.stdin.readline

def isBalance(s):
    stack = []
    for chr in s:
        if chr == '(' or chr == '[':
            stack.append(chr)
        elif chr == ')' or chr == ']':
            # 닫는 괄호가 여는 괄호보다 먼저 나오면 불균형
            if not stack:
                return 'no'
            open = stack.pop()
            # 여는 괄호와 닫는 괄호가 매칭이 안되면 불균형
            if (open == '(' and chr == ']') or (open == '[' and chr == ')'):
                return 'no'
    return 'no' if stack else 'yes'

while True:
    s = input().rstrip()
    if s == '.':
        break
    print(isBalance(s))