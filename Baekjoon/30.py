# 30
from functools import reduce
import sys

nums = list(sys.stdin.readline().rstrip())

if '0' in nums and reduce(lambda x, y: int(x)+int(y), nums)%3 == 0:
    print(''.join(sorted(nums, reverse=True)))
else:
    print(-1)