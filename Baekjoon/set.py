# 집합
import sys
input = sys.stdin.readline
s = set()
m = int(input().rstrip())
for _ in range(m):
    operation = input().split()
    op = operation[0]
    if len(operation) == 2:
        num = int(operation[1])
        if op == 'add' and num not in s:
            s.add(num)
        elif op == 'remove' and num in s:
            s.remove(num)
        elif op == 'check':
            if num in s:
                print(1)
            else:
                print(0)
        elif op == 'toggle':
            if num in s:
                s.remove(num)
            else:
                s.add(num)
    else:
        if op == 'all':
            s = set(range(1, 21))
        else:
            s = set()