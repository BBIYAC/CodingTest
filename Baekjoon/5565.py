import sys
input = sys.stdin.readline

total = int(input().rstrip())
for _ in range(9):
    total -= int(input().rstrip())

print(total)