# 알파벳 개수
import sys
s = sys.stdin.readline().rstrip()
alphabet = [0]*26
for alpha in s:
    alphabet[ord(alpha)-97] += 1

print(*alphabet)