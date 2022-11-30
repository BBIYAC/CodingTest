# [프로그래머스] 다음 큰 숫자
def solution(n):
    next_n = n + 1
    while True:
        if bin(n).count('1') == bin(next_n).count('1'):
            break
        else:
            next_n += 1        
    return next_n