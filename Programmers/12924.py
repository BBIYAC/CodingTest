# [프로그래머스] 숫자의 변환
def solution(n):
    answer = 0
    numArray = list(range(1, n + 1))
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if sum(numArray[i-1:j]) == n:
                answer += 1
    return answer

# 시간 초과 에러 해결
def solution(n):
    answer = 0
    numArray = list(range(1, n + 1))
    i, j = 0, 0
    while i < n:
        sumResult = sum(numArray[i:j])
        if sumResult > n:
            i += 1
        elif sumResult < n:
            j += 1
        else:
            answer += 1
            i += 1
    return answer