# 별 찍기
'''
문제
재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.
크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.
N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다. 
예를 들어 크기 27의 패턴은 예제 출력 1과 같다.

입력
첫째 줄에 N이 주어진다. N은 3의 거듭제곱이다. 즉 어떤 정수 k에 대해 N=3k이며, 이때 1 ≤ k < 8이다.

출력
첫째 줄부터 N번째 줄까지 별을 출력한다.
'''
import sys

def star(n, s):
    stars = []
    if n==3:
        return s
    else:
        for i in s: # 첫 번째 구역
            stars.append(i*3)
        for i in s: # 가운데 구역
            stars.append(i+' '*len(s)+i)
        for i in s: # 마지막 구역
            stars.append(i*3)
    return star(n//3, stars)

# 정수 N
n = int(sys.stdin.readline().rstrip())
for str in star(n, ['***', '* *', '***']):
    print(str)