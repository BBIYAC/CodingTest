# 팰린드롬 수
import sys
while 1:
    num = sys.stdin.readline().rstrip()
    isPalindrom = 'yes'
    if num == '0':
        break
    for i in range(len(num)//2):
        if num[i] != num[-i-1]:
            isPalindrom = 'no'
            break

    print(isPalindrom)