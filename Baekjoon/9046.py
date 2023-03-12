# [백준 9046] 복호화

import sys
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    string = input().rstrip()
    cipher = [0] * 26
    for char in string:
        if char.isalpha():
            cipher[ord(char)-ord('a')] += 1
    count = max(cipher)
    print(chr(ord('a') + cipher.index(count)) if cipher.count(count) < 2 else '?')