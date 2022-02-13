'''
부품 찾기
M개 종류의 부품 N개를 구입하려할 때 가게 안에 부품이 모두 있는지 확인
부품 번호의 순서대로 부품을 확인해 부품이 있으면 yes, 없으면 no

# 입력 조건
1. 첫째 줄에 정수 N
2. 둘째 줄에 공백으로 구분하여 N개의 정수
3. 셋째 줄에 정수 M
4. 넷째 줄에 공백으로 구분하여 M개의 정수

# 출력 조건
공백으로 구분하여 각 부품이 존재하면 yes, 없으면 no

# 입력 예시
5
8 3 7 9 2
3
5 7 9

# 출력 예시
no yes yes
'''

n = int(input('>> '))
arrayN = list(map(int, input('>> ').split()))
m = int(input('>> '))
arrayM = list(map(int, input('>> ').split()))

# 특정 데이터 포함 여부 판단 풀이법
def solution():
    answer = ''
    for m in arrayM:
        # arrayN 안에 요청한 부품 m이 포함되어 있으면
        if m in arrayN:
            answer += 'yes '
        else: # 부품이 포함되어 있지 않으면
            answer += 'no '
    return answer

print('특정 문자 포함 풀이법:', solution())

# 이진 탐색 풀이법
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        # 부품을 찾은 경우 중간 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점(array[mid])의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid-1
        else: # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
            start = mid+1
    return None

def binary_solution():
    answer = ''
    array = sorted(arrayN)
    for part in arrayM:
        # 해당 부품이 존재하는지 확인
        check = binary_search(array, part, 0, n-1)
        if check != None:
            answer += 'yes '
        else:
            answer += 'no '
    return answer

print('이진 탐색 풀이법:', binary_solution())