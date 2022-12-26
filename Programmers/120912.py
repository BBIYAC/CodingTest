# [프로그래머스] 문자열 밀기
def solution(A, B):
    count = 0
    for _ in range(len(A)):
        if A == B:
            return count
        A = A[-1] + A[:-1]
        count += 1
        
    return -1