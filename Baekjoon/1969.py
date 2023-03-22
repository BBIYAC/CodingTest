# [백준 1969] DNA

import sys
input = sys.stdin.readline

# DNA의 수 N, 문자열의 길이 M
N, M = map(int, input().split())
DNA = [input().rstrip() for _ in range(N)]

# 최소 Hamming Distance
HD = 0
HD_DNA = ''

for i in range(M):
    ACGT = [0, 0, 0, 0]
    for j in range(N):
        if DNA[j][i] == 'A':
            ACGT[0] += 1
        elif DNA[j][i] == 'C':
            ACGT[1] += 1
        elif DNA[j][i] == 'G':
            ACGT[2] += 1
        elif DNA[j][i] == 'T':
            ACGT[3] += 1
    
    # 가장 많이 나온 문자 인덱스
    max_idx = ACGT.index(max(ACGT))

    if max_idx == 0:
        HD_DNA += 'A'
    elif max_idx == 1:
        HD_DNA += 'C'
    elif max_idx == 2:
        HD_DNA += 'G'
    elif max_idx == 3:
        HD_DNA += 'T'
    # N - 가장 많이 나온 문자 수
    HD += N - max(ACGT)

print(HD_DNA)
print(HD)