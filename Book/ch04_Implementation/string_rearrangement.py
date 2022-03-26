'''
문자열 재정렬
알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어짐
모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤, 그 뒤에 모든 숫자를 더한 값을 이어서 출력

# 입력 조건
하나의 문자열 s가 주어짐

# 출력 조건
문제에서 요구하는 정답

# 입력 예시 1
K1KA5CB7

# 출력 예시 1
ABCKK13

# 입력 예시 2
AJKDLSI412K4JSJ9D

# 출력 예시 2
ADDIJJJKKLSS20
'''

def solution():
    answer = ''
    # 문자열 s
    string = sorted(input('>> '))
    # 숫자들의 합
    num = 0
    # 문자열 하나씩 숫자인지 확인
    for s in string:
        # 숫자면 숫자들의 합에 +
        if s.isdigit():
            num += int(s)
        else: # 문자면 정답에 +
            answer += s
    if num != 0:
        answer += str(num)
    return answer

print(solution())


# 정답
def answer_solution():
    data = input('>> ')
    result = []
    value = 0

    # 문자 하나씩 확인
    for x in data:
        # 알파벳인 경우 결과 리스트에 삽입
        if x.isalpha():
            result.append(x)
        # 숫자는 따로 더하기
        else:
            value += int(x)

    # 알파벳을 오름차순으로 정렬
    result.sort()

    # 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
    if value != 0:
        result.append(str(value))

    # 최정 결과 출력
    return ''.join(result)

print(answer_solution())    