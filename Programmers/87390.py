# [프로그래머스] N2 배열 자르기
def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        a, b = divmod(i, n)
        answer.append(max(a, b)+1)
    
    return answer