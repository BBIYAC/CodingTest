# [백준 11365] !밀비 급일

import sys
input = sys.stdin.readline

while True:
    string = input().rstrip()
    if string == 'END': break
    print(string[::-1])