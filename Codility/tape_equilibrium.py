# [코딜리티] Tape Equilibrium
def solution(A):
    min_gap = 1e9
    len_A = len(A)
    sum_A = [0]*len_A
    for i in range(len_A):
        sum_A[i] = A[i] if i==0 else sum_A[i-1] + A[i]

    for P in range(1, len_A):
        gap = abs(sum_A[len_A-1] - 2*sum_A[P-1])
        min_gap = min(min_gap, gap)

    return min_gap
    
print(solution([3, 1, 2, 4, 3]))
print(solution([1, 1]))