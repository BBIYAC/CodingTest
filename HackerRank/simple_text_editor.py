# [해커랭크] Simple Text Editor
import sys
input = sys.stdin.readline

S = ""
Q = int(input().rstrip())
history = []
for _ in range(Q):
    inputs = input().split()
    if inputs[0] == '1':
        history.append(S)
        S += inputs[1]
    elif inputs[0] == '2':
        history.append(S)
        S = S[:-int(inputs[1])]
    elif inputs[0] == '3':
        print(S[int(inputs[1])-1])
    elif inputs[0] == '4':
        S = history.pop()

        