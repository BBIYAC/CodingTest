'''
바닥 공사
2 x n인 직사각형 바닥을 1x2, 2x1, 2x2의 덮개를 이용해 채우고자할 때 모든 경우의 수

# 입력 조건
n이 주어진다

# 출력 조건
2 x n인 바닥을 채우는 방법의 수를 796796으로 나눈 나머지를 출력

# 입력 예시
3

# 출력 에시
5
'''

# 가로의 길이 n 입력
n = int(input('>> '))
# 덮개의 종류 입력
tiles = [(1, 2), (2, 1), (2, 2)]

def dp_solution():
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n+1):
        dp[i] = (dp[i-1]+2*dp[i-2]) % 796796
        print(dp)
    return dp[n]

print(dp_solution())