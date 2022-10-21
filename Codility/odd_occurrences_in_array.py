# [코딜리티] Odd Occurrences In Array
def solution(A):
    A.sort()
    answer = 0
    for i in range(0, len(A)-1, 2):
        if A[i] != A[i+1]:
            answer = A[i]
            break
    return answer if answer else A[-1]

print(solution([2, 2, 3, 3, 4]))