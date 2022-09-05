# 뒤집기
import sys
nums = sys.stdin.readline().rstrip()
one, zero = 0, 0

if nums[0] == '0':
    zero = 1
else:
    one = 1

for i, num in enumerate(nums[1:], start=1):
    if num != nums[i-1]:
        if num == '1': # 1을 0으로 변환
            one += 1
        else: # 0을 1로 변환
            zero += 1

print(min(one, zero))