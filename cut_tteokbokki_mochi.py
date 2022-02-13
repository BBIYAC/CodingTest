'''
떡볶이 떡 만들기
절단기에 높이(H)를 지정하면 줄지어진 떡을 한번에 절단한다.
손님이 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값

# 입력 조건
1. 첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다
2. 둘째 줄에는 떡의 개별 높이가 주어진다.

# 출력 조건
적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값

# 입력 예시
4 6
19 15 10 17

# 출력 예시
15
'''

# 정렬 후 탐색 방법
n, m = map(int, input('>> ').split())
rice_cakes = list(map(int, input('>> ').split()))

def solution():
    answer = 0
    count = 0
    array = sorted(rice_cakes, reverse=True)
    for i, h in enumerate(array):
        for j in range(i):
            count += array[j]-h
        if count >= m:
            answer = h
            break
    return answer

print(solution())

# 이진 탐색법
def binary_solution():
    answer = 0
    # 이진 탐색을 위한 시작점과 끝점
    start = 0
    end = max(rice_cakes)
    # 이진 탐색 수행
    while(start<=end):
        total = 0
        mid = (start+end)//2
        for h in rice_cakes:
            # 잘랐을 때의 떡의 양 계산
            if h > mid:
                total += h-mid
        # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 탐색)
        if total < m:
            end = mid-1
        else: # 떡의 양이 충분한 경우 덜 자르기(오른쪽 탐색)
            answer = mid # 최대한 덜 잘랐을 때가 정답
            start = mid+1
    return answer

print(binary_solution())