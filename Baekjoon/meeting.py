# 회의룸 배정
'''
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14

4
'''

import sys
input = sys.stdin.readline

n = int(input())
n_arr = sorted([tuple(map(int, input().split())) for _ in range(n)], key = lambda x: (x[1], x[0]))
count = 1
end = n_arr[0][1]
for (next_s, next_e) in n_arr[1:]:
    if next_s >= end:
        count += 1
        end = next_e

print(count)