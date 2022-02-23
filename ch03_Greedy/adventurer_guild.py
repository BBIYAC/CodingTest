'''
모험가 길드
N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값
공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있음.

# 입력 조건
1. 첫째 줄에 모험가 수 N
2. 둘째 줄에 각 모험가의 공포도 값을 N이하의 자연수로 공백 구분

# 출력 조건
여행을 떠날 수 있는 그룹 수의 최댓값 출력

# 입력 예시
5
2 3 1 2 2

# 출력 예시
2
'''

def solution():
    # 총 그룹의 수
    maximum = 0
    i = 0
    # 모험가 수
    n = int(input('>> '))
    # 각 모험가의 공포도 값
    adventurer = list(map(int, input('>> ').split()))
    # 공포도 내림차순 정렬
    adventurer.sort(reverse=True)
    # 그룹에서 가장 큰 공포도 만큼의 사람을 한 그룹으로 지정
    while n>0:
        maximum += 1
        n -= adventurer[i]
        i += adventurer[i]

    return maximum

print(solution())

def answer():
    n = int(input('>> '))
    data = list(map(int, input('>> ').split()))
    data.sort()

    result = 0 # 총 그룹의 수
    count = 0 # 현재 그룹에 포함된 모험가의 수

    for i in data: # 공포도를 낮은 것부터 하나씩 확인
        count += 1 # 현재 그룹에 해당 모험가 포함
        if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
            result += 1 # 총 그룹의 수 증가시키기
            count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

    return result

print(answer())