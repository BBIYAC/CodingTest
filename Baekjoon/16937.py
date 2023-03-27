# [백준 16937] 두 스티커

import sys
input = sys.stdin.readline

# 모눈종이의 크기 H, W
H, W = map(int, input().split())
# 스티커의 수 N
N = int(input().rstrip())
# 스티커의 크기 Ri, Ci
stickers = [list(map(int, input().split())) for _ in range(N)]

# 4가지 케이스 테스트 함수
def isCase(a, b, c, d):
    return (a+b <= H and max(c, d) <= W) or (max(a, b) <= H and c+d <= W)

answer = 0
for i in range(N):
    for j in range(i+1, N):
        R1, C1 = stickers[i]
        R2, C2 = stickers[j]

        true_case = [isCase(R1, R2, C1, C2), # 둘 다 회전하지 않을 경우
                     isCase(C1, R2, R1, C2), # 첫번째 스티커만 회전하는 경우
                     isCase(R1, C2, C1, R2), # 두번째 스티커만 회전하는 경우
                     isCase(C1, C2, R1, R2)] # 둘 다 회전하는 경우
        
        if sum(true_case) > 0:
            answer = max(answer, R1*C1 + R2*C2)

print(answer)