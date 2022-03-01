'''
문자열 압축
문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여
더 짧은 문자열로 줄여서 표현하는 알고리즘

# 입력 예시 1
'aabbaccc'

# 출력 예시 1
7

# 입력 예시 2
'ababcdcdabcdcd'

# 입력 예시 2
9

# 입력 예시 3
'abcabcdede'

# 출력 예시 3
8

# 입력 예시 4
'abcabcabcabcdededededede'

# 출력 예시 4
14

# 입력 예시 5
'xababcdcdababcdcd'

# 출력 예시 5
17
'''

# def solution(s):
#     answer = len(s)
#     for i in range(1, len(s)//2+1):
#         count = 1
#         string = ''
#         for j in range(i, len(s), i):
#             # 같은 문자열 연속되면
#             if s[j:j+i] == s[j-i:j]:
#                 count += 1
#             # 같은 문자열이 2개 이상이면
#             elif count > 1: 
#                 string += str(count)+s[j-i:j]
#                 count = 1
#             else: # 같은 문자열이 없으면
#                 string += s[j-i:j]
#         # 나머지 문자열
#         string += str(count) + s[-i:] if count > 1 else s[-i:]
#         answer = min(len(string), answer)
#     return answer

# print('1:', solution('aabbaccc'))
# print('2:', solution('ababcdcdabcdcd'))
# print('3:', solution('abcabcdede'))
# print('4:', solution('abcabcabcabcdededededede'))
# print('5:', solution('xababcdcdababcdcd'))


def answer_solution(s):
    answer = len(s)
    # 1개 단위부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s)//2+1):
        compressed = ''
        prev = s[0:step] # 앞에서부터 step만큼의 문자열 추출
        count = 1
        # 단위 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 횟수 증가
            if prev == s[j:j+step]:
                count += 1
            # 다른 문자열이 나왔다면
            else:
                compressed += str(count) + prev if count>=2 else prev
                prev = s[j:j+step]
                count = 1

        # 남아 있는 문자열에 대해 처리
        compressed += str(count) + prev if count>=2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정담
        answer = min(answer, len(compressed))
    return answer

print('1:', answer_solution('aabbaccc'))
print('2:', answer_solution('ababcdcdabcdcd'))
print('3:', answer_solution('abcabcdede'))
print('4:', answer_solution('abcabcabcabcdededededede'))
print('5:', answer_solution('xababcdcdababcdcd'))