'''
두 배열의 원소 교체
N개의 원소로 구성된 배열 A, B가 있고, 최대 K번의 바꿔치기 연산 수행 가능
배열 A의 모든 원소의 합이 최대가 되도록 하는 프로그램

# 입력 조건
1. 첫 번째 줄 N, K 공백 구분
2. 두 번째 줄에 배열 A의 원소들이 공백으로 구분
3. 세 번째 줄에 배열 B의 원소들이 공백으로 구분

# 출력 조건
최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값 출력

# 입력 예시
5 3
1 2 5 4 3
5 5 6 6 5

# 출력 예시
26
'''

n, k = map(int, input('>> ').split())
arrayA = list(map(int, input('>> ').split()))
arrayB = list(map(int, input('>> ').split()))


def solution():
    # A 배열 오름차순 정렬
    arrayA.sort()
    # B 배열 내림차순 정렬
    arrayB.sort(reverse=True)
    # 최대 K번 반복
    for i in range(k):
        # 배열 A와 B 요소를 차례로 비교
        if arrayA[i]<arrayB[i]:
            # temp를 이용한 요소 교체와 같음
            arrayA[i], arrayB[i] = arrayB[i], arrayA[i] 
        else: # 배열 A의 요소가 B요소보다 크거나 같으면 반복 종료
            break
    return sum(arrayA) # 배열 A의 요소들의 합

print(solution())