# [프로그래머스] 인덱스 바꾸기
def solution(my_string, num1, num2):
    answer = list(my_string)
    answer[num2], answer[num1] = answer[num1], answer[num2]
    return ''.join(answer)