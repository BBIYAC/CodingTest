# [백준 1032] 명령 프롬프트
import sys
input = sys.stdin.readline

n = int(input().rstrip())
fileNames = [input().rstrip() for _ in range(n)]
for i, char in enumerate(fileNames[0]):
    check = True
    for fileName in fileNames:
        if fileName[i] != char:
            check = False
            break
    if check:
        print(char, end='')
    else:
        print('?', end='')
