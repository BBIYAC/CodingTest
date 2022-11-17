# [프로그래머스] 최솟값 만들기
def solution(A,B):
    answer = 0
    sortA = sorted(A)
    sortB = sorted(B, reverse=True)

    for i in range(len(A)):
        answer += sortA[i] * sortB[i]

    return answer