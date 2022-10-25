# [백준 2587] 대표값2
import sys
array = [int(sys.stdin.readline().rstrip()) for _ in range(5)]

print(sum(array)//len(array))
print(sorted(array)[len(array)//2])