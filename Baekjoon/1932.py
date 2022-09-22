# [백준 1932] 정수 삼각형
import sys
input = sys.stdin.readline

n = int(input().rstrip())
triangle = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(i+1):
        if (i, j) == (0, 0):
            continue
        elif j == 0:
            triangle[i][j] += triangle[i-1][j]
        elif j == i:
            triangle[i][j] += triangle[i-1][j-1]
        else:
            triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])

print(max(triangle[n-1]))