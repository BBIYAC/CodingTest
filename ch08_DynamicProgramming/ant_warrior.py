'''
개미 전사
개미 전사가 정찰병에게 들키지 않고 식량창고 N개에 대한 정보가 주어졌을 때
얻을 수 있는 식량의 최댓값을 구하는 프로그램.
정찰병에게 들키지 않으려면 한 칸 이상 떨어진 식량 창고를 약탈해야 함.

# 입력 조건
1. 첫째 줄에 식량 창고의 개수 N
2. 둘째 줄에 공백으로 구분되어 각 식량 창고에 저장된 식량의 개수 K

# 출력 조건
첫째 줄에 개미 전사가 얻을 수 있는 식량의 최댓값

# 입력 예시
4
1 3 1 5

# 출력 예시
8
'''

# 식량 창고의 개수
n = int(input('>> '))
# 각 식량 창고에 저장된 식량의 개수
counts = list(map(int, input('>> ').split()))

def solution():
    max_food = 0
    for i in range(n-1):
        for j in range(i+2, n):
            food = counts[i]+counts[j]
            max_food = max(food, max_food)
    return max_food

print(solution())

# 다이나믹 프로그래밍 활용 풀이법
def dp_solution():
    dp = [0]*(n+1)
    dp[0] = counts[0]
    dp[1] = max(counts[0], counts[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2]+counts[i])
    return dp[n-1]

print(dp_solution())