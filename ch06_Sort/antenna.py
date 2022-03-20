'''
안테나
집들의 위치 값이 주어질 때 안테나로부터 모든 집까지의 거리의 총합이 최소가 되도록 설치할 위치를 선택하는 프로그램

# 입력 예시
4
5 1 7 9

# 출력 예시
5
'''

def solution():
    n = int(input('>> '))
    # 집 위치
    homes = list(map(int, input('>> ').split()))
    # 안테나 설치 위치
    min_distance = {}
    for home in homes:
        distance = 0
        for antenna in homes:
            distance += abs(antenna - home)
        min_distance[home] = distance
    # 안테나 설치할 총합 최소 위치
    answer = min(min_distance, key=min_distance.get)
    return answer

print(solution())