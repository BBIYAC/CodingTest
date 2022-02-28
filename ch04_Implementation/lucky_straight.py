'''
럭키 스트레이트
현재 캐릭터의 점수를 N이라고 할 때 자릿수를 기준으로 점수 N을 반으로 나누어
왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황을 의미함

현재 점수 N이 주어지면 럭키 스트레이트를 사용할 수 있는 상태인지 아닌지를 알려주는 프로그램

# 입력 조건
점수 N이 정수로 주어짐(자릿수는 짝수 형태)

# 출력 조건
럭키 스트레이트를 사용할 수 있다면 'LUCKY', 사용할 수 없다면 'READY' 출력

# 입력 예시 1
123402

# 출력 예시 1
LUCKY

# 입력 예시 2
7755

# 출력 예시 2
READY
'''

def solution():
    # 점수 n
    n = input('>> ')

    # 절반, 왼쪽, 오른쪽
    center, left, right = len(n)//2, 0, 0
    for i in range(center):
        left += int(n[i]) # 왼쪽 카운트
        right += int(n[center+i]) # 오른쪽 카운트

    # 왼쪽 합과 오른쪽 합이 같으면
    if left == right:
        return 'LUCKY'
    else:
        return 'READY'

print(solution())