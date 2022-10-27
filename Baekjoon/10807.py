# [백준 10807] 개수 세기
import sys
input = sys.stdin.readline

N = int(input().rstrip())
array = list(map(int, input().split()))
v = int(input().rstrip())

print(array.count(v))