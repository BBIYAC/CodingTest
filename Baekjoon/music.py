# 음계
import sys
origin = list(map(int, sys.stdin.readline().split()))
asc = sorted(origin)
desc = sorted(origin, reverse=True)
if origin == asc:
    print('ascending')
elif origin == desc:
    print('descending')
else:
    print('mixed')