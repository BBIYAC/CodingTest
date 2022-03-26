'''
문자열 뒤집기
0과 1로 이루어진 문자열 S에 있는 모든 숫자를 전부 같게 만들려 할 때,
S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는다.

# 입력 조건
0과 1로만 이루어진 문자열 S

# 출력 조건
최소 행동 횟수

# 입력 예시
0001100

# 출력 예시
1
'''

def solution():
    # 0과 1로만 이루어진 문자열 s
    s = input('>> ')
    # 시작하는 문자가 0인지 1인지에 따라 count
    cnt_zero = 1 if int(s[0]) == 0 else 0
    cnt_one = 1 if int(s[0]) == 1 else 0
    # 문자 하나씩 비교
    for i in range(1, len(s)):
        # 이전 값과 비교
        if s[i-1] != s[i]:
            # 다음 값이 0이면
            if s[i] == '0':
                cnt_zero += 1
            else: # 다음 값이 1이면
                cnt_one += 1
    answer = min(cnt_zero, cnt_one)
    return answer
print(solution())