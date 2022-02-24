'''
곱하기 혹은 더하기
각 자리 숫자(0부터 9)로만 이루어진 문자열 S가 주어졌을 때,
왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'x' 혹은 '+'연산자를 넣어 
결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램

# 입력 조건
여러 개의 숫자로 구성된 하나의 문자열 S

# 출력 조건
만들어질 수 있는 가장 큰 수 출력

# 입력 예시 1
02984

# 출력 예시 1
576

# 입력 예시 2
567

# 출력 예시 2
210
'''

def solution():
    answer = 1
    # 각 자리 숫자(0부터 9)로만 이루어진 문자열
    s = input('>> ')
    # 각 자리 숫자 비교
    for str in s:
        # 숫자로 변환
        num = int(str)
        # 가장 큰 수를 만들기 위해 숫자가 0이면 '+'
        if num == 0:
            answer += num
        else: # 0이 아니면 'x'
            answer *= num
    return answer

print(solution())