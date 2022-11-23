# [프로그래머스] 숫자의 변환
def solution(n):
    answer = 0
    numArray = list(range(1, n + 1))
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if sum(numArray[i-1:j]) == n:
                answer += 1
    return answer