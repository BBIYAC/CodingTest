# [백준 25501] 재귀의 귀재
import sys
input = sys.stdin.readline

def recursion(s, l, r, count):
    if l >= r: return [1, count]
    elif s[l] != s[r]: return [0, count]
    else: return recursion(s, l+1, r-1, count+1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 1)

t = int(input().rstrip())
for _ in range(t):
    s = input().rstrip()
    print(*isPalindrome(s))