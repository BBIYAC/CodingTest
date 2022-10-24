# [백준 10988] 팰린드롬인지 확인하기
import sys
word = sys.stdin.readline().rstrip()
print(1 if word == word[::-1] else 0)