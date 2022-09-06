# 생일

import sys
input = sys.stdin.readline

n = int(input().rstrip())
# 이름 dd mm yyyy
datas = sorted([list(input().split()) for _ in range(n)], key=lambda x: (-int(x[3]), -int(x[2]), -int(x[1])))
# 나이가 가장 적은 사람
print(datas[0][0])
# 나이가 가장 많은 사람
print(datas[-1][0])
    