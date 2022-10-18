# [백준 1212] 8진수 2진수

import sys
digit_8 = sys.stdin.readline().rstrip()
digit_10 = int(digit_8, 8)
digit_2 = bin(digit_10)
print(digit_2[2:])