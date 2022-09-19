# 문자열
import sys
input = sys.stdin.readline

n = int(input().rstrip())
for _ in range(n):
    string = input().rstrip()
    print(string[0]+string[-1])