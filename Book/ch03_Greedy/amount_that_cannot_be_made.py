'''
만들 수 없는 금액
N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값

# 입력 조건
1. 동전의 개수를 나타내는 양의 정수 N
2. 각 동전의 화폐 단위를 나타내는 N개의 자연수

# 출력 조건
주어진 동전들로 만들 수 없는 양의 정수 금액 중 최솟값

# 입력 예시
5
3 2 1 1 9

# 출력 예시
8
'''

def solution():
    # 동전의 개수 n
    n = int(input('>> '))
    # 각 동전의 화폐 단위
    array = sorted(map(int, input('>> ').split()))
    amount = 1
    for money in array:
        if amount < money:
            break
        amount += money
    
    return amount

print(solution())