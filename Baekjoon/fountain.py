# 분수 찾기

import sys
n = int(sys.stdin.readline().rstrip())

num = 0
num_count = 0

while num_count < n:
    num += 1
    num_count += num

num_count -= num

if num % 2 == 0:
    numerator = n - num_count
    denominator = num - numerator + 1
else:
    numerator = num - (n - num_count) + 1
    denominator = n - num_count

print("{}/{}".format(numerator, denominator))