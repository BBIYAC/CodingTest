'''
위에서 아래로
수열을 내림차순으로 정렬하는 프로그램

# 입력 조건
1. 첫째 줄에 수열에 속해 있는 수의 개수 N이 주어진다.
2. 둘째 줄부터 N+1번째 줄까지 N개의 수 입력

# 출력 조건
입력으로 주어진 수열이 내림차순으로 정렬된 결과를 공백으로 구분하여 출력

# 입력 예시
3
15
27
12

# 출력 예시 
27 15 12

## 파이썬 내장함수 sorted 사용
# sort()와 sorted 차이
# a.sort(): 원본 리스트를 정렬
# sorted(a): 새로운 리스트에 원본 리스트를 정렬하여 반환
'''

n = int(input('>> '))
array = []
for i in range(n):
    array.append(int(input('>> ')))

def solution(n, array):
    arr = sorted(array, reverse=True)
    answer = ''
    for i in range(n):
        answer = (str(arr[i]) if i==0 else answer+' '+str(arr[i]))
    return answer

print(solution(n, array))