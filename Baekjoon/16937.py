# [백준 16937] 두 스티커

import sys
input = sys.stdin.readline

# 모눈종이의 크기 H, W
H, W = map(int, input().split())
# 스티커의 수 N
N = int(input().rstrip())
# 스티커의 크기 Ri, Ci
stickers = [list(map(int, input().split())) for _ in range(N)]

answer = 0
for i in range(N):
    for j in range(i+1, N):
        R1, C1 = stickers[i]
        R2, C2 = stickers[j]

        # 둘 다 회전하지 않을 경우
        if (R1+R2 <= H and max(C1, C2) <= W) or (max(R1, R2) <= H and C1+C2 <= W):
            answer = max(answer, R1*C1 + R2*C2)
        # 첫번째 스티커만 회전하는 경우
        if (C1+R2 <= H and max(R1, C2) <= W) or (max(C1, R2) <= H and R1+C2 <= W):
            answer = max(answer, R1*C1 + R2*C2)
        # 두번째 스티커만 회전하는 경우
        if (R1+C2 <= H and max(C1, R2) <= W) or (max(R1, C2) <= H and C1+R2 <= W):
            answer = max(answer, R1*C1 + R2*C2)
        # 둘 다 회전하는 경우
        if (C1+C2 <= H and max(R1, R2) <= W) or (max(C1, C2) <= H and R1+R2 <= W):
            answer = max(answer, R1*C1 + R2*C2)

print(answer)