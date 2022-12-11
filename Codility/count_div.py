# [코딜리티] Count Div
def solution(A, B, K):
    answer = (B // K) - (A // K)
    if (A % K) == 0:
      answer += 1
    return answer

print(solution(2, 2, 2)) # 2
print(solution(0, 13, 12)) # 2
print(solution(6, 12, 6)) # 2
print(solution(6, 11, 2)) # 3
print(solution(11, 345, 17)) # 20