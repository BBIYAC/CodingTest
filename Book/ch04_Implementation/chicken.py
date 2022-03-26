'''
치킨 배달
크기가 N x N인 도시가 있고, 도시의 칸은 (r, c)와 같은 형태로 의미하며 r행 c열 또는 위에서 r번째 칸, 왼쪽에서부터 c번째 칸을 의미한다.
치킨 거리: 집과 가장 가까운 치킨 집 사이의 거리
도시의 치킨 거리: 모든 집의 치킨 거리의 합
임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 abs(r1-r2) + abs(c1-c2)
이 때 도시의 치킨 거리가 가장 작게되는 프로그램

# 입력 조건
1. 첫째 줄에 N, M
2. 둘째 줄부터 N개의 줄에는 도시의 정보가 주어짐
3. 도시의 정보는 0, 1, 2로 이루어져 있고, 0은 빈칸, 1은 집, 2는 치킨집을 의미함
   집의 개수는 2N개를 넘지 않으며, 적어도 1개는 존재함.
   치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같음

# 출력 조건
폐업시키지 않을 치킨집을 최대 M개 골랐을 때, 도시의 치킨 거리의 최솟값 출력

# 입력 예시 1
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2

# 출력 예시 1
5

# 입력 예시 2
5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2

# 출력 예시 2
10

# 입력 예시 3
5 1
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0

# 출력 예시 3
11

# 입력 예시 4
5 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1

# 출력 예시 4
32
'''

from itertools import combinations

def solution():
    n, m = map(int, input('>> ').split())
    chicken, house = [], []
    for r in range(n):
        data = list(map(int, input('>> ').split()))
        for c, d in enumerate(data):
            if d == 1:
                house.append((r, c)) # 집
            elif d == 2:
                chicken.append((r, c)) # 치킨집

    # 모든 치킨집 중 m개의 치킨집을 뽑는 조합
    candidates = list(combinations(chicken, m))

    answer = 1e9
    for candidate in candidates:
        result = 0
        for hx, hy in house:
            temp = 1e9
            for cx, cy in candidate:
                temp = min(temp, abs(hx-cx)+abs(hy-cy))
            result += temp
        answer = min(answer, result)

    return answer

print(solution())


# 정답

# n, m = map(int, input('>> ').split())
# chicken, house = [], []
# for r in range(n):
#     data = list(map(int, input('>> ').split()))
#     for c in range(n):
#         if data[c] == 1:
#             house.append((r, c)) # 집
#         elif data[c] == 2:
#             chicken.append((r, c)) # 치킨집

# # 모든 치킨집 중 m개의 치킨집을 뽑는 조합
# candidates = list(combinations(chicken, m))


# # 치킨 거리의 합을 계산하는 함수
# def get_sum(candidate):
#     result = 0
#     # 모든 집에 대하여
#     for hx, hy in house:
#         # 가장 가까운 치킨집 찾기
#         temp = 1e9
#         for cx, cy in candidate:
#             temp = min(temp, abs(hx-cx)+abs(hy-cy))
#         # 가장 가까운 치킨집까지의 거리 더하기
#         result += temp
#     # 치킨 거리의 합 반환
#     return result

# def answer_solution():
#     answer = 1e9
#     for candidate in candidates:
#         answer = min(answer, get_sum(candidate))
#     return answer

# print(answer_solution())