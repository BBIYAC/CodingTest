# [프로그래머스] 이진 변환 반복하기
def solution(s):
    answer = [0, 0]
    while s != '1':
        prev = len(s)
        removeZero = len(s.replace('0', ''))
        s = bin(removeZero)[2:]
        answer[0] += 1
        answer[1] += prev - removeZero
    return answer

print(solution("110010101001"))