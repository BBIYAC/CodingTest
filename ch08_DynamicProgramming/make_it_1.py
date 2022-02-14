'''
1로 만들기
1. 정수 N이 5로 나누어떨어지면, 5로 나눈다.
2. N이 3으로 나누어떨어지면, 3으로 나눈다.
3. N이 2로 나누어떨어지면, 2로 나눈다.
4. N에서 1을 뺀다.

위 연산 방법 4개를 적절히 사용해서 1을 만들 때, 연산 사용 최솟값을 출력

# 입력 조건
정수 N이 주어진다.

# 출력 조건
연산을 하는 횟수의 최솟값 출력

# 입력 예시
26

# 출력
3
'''
n = int(input('>> '))

# 다이나믹 프로그래밍
def dp_solution():
    d = [0]*30001
    for i in range(2, n+1):
        # 현재의 수에서 1을 빼는 경우
        d[i] = d[i-1]+1
        # 현재의 수가 2로 나누어 떨어지는 경우
        if i%2 == 0:
            d[i]=min(d[i],d[i//2]+1)
        # 현재의 수가 3으로 나누어 떨어지는 경우
        if i%3 == 0:
            d[i]=min(d[i],d[i//3]+1)
        # 현재의 수가 5로 나누어 떨어지는 경우
        if i%5 == 0:
            d[i]=min(d[i],d[i//5]+1)
    return d[n]

print(dp_solution())

# 재귀 함수 활용
count = 0
def division(n):
    global count
    if n>1:
        count += 1
        if n%5 <= 1:
            division(n//5) if n%5==0 else division(n-1)
        elif n%3 == 0:
            division(n//3)
        elif n%2 == 0:
            division(n//2)
        return count
print(division(n))