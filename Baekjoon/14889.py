# [백준 14889] 스타트와 링크
'''
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0

0
--------
6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0

2
---------
8
0 5 4 5 4 5 4 5
4 0 5 1 2 3 4 5
9 8 0 1 2 3 1 2
9 9 9 0 9 9 9 9
1 1 1 1 0 1 1 1
8 7 6 5 4 0 3 2
9 1 9 1 9 1 0 9
6 5 4 3 2 1 9 0

1
'''
import copy
from itertools import combinations
import sys
input = sys.stdin.readline

# 인덱스 리스트
n = list(range(int(input().rstrip())))
# 그래프
graph = [list(map(int, input().split())) for _ in n]

# 스타트와 링크 점수 차이 최솟값
min_score = 1e9

# 스타트와 링크 반으로 나누는 경우의 수
sl_combi = list(combinations(n, len(n)//2))
for start in sl_combi[:len(sl_combi)//2]:
    link = copy.deepcopy(n)
    for num in start:
        link.remove(num)
    # 스타트와 링크 각각 두 개씩 뽑아 (i, j) 생성
    s_combi = list(combinations(start, 2))
    l_combi = list(combinations(link, 2))
    # 스타트 점수와 링크 점수
    s_score, l_score = 0, 0
    # 각 팀의 능력치 더하기
    for i in range(len(s_combi)):
        (si, sj) = s_combi[i]
        (li, lj) = l_combi[i]
        s_score += graph[si][sj] + graph[sj][si]
        l_score += graph[li][lj] + graph[lj][li]
    # 스타트와 링크 능력치 차이
    gap = abs(s_score - l_score)
    # 능력치 차이 갱신
    if gap < min_score:
        min_score = gap

print(min_score)