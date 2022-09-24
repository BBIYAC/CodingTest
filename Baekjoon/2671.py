# 잠수함 식별
'''
(100~1~|01)~
'''
import re
import sys
string = sys.stdin.readline().rstrip()
if re.fullmatch('(100+1+|01)+', string) == None:
    print("NOISE")
else:
    print("SUBMARINE")