# [프로그래머스] 콜라 문제
def solution(a, b, n):
    answer = 0
    while n > a - 1:
        mart = (n // a) * b
        answer += mart
        n = (n % a) + mart
        
    return answer

print(solution(2, 1, 20)) # 19
print(solution(3, 1, 20)) #9