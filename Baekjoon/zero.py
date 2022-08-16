# 제로
import sys
input = sys.stdin.readline

K = int(input().rstrip())
numbers = []
for _ in range(K):
    number = int(input().rstrip())
    if number != 0:
        numbers.append(number)
    else:
        numbers.pop()

print(sum(numbers))