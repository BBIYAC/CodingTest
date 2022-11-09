# [프로그래머스] 3진법 뒤집기
def solution(n):
    number = ''
    while n > 0:
        div, mod = divmod(n, 3)
        n = div
        number += str(mod)
        
    return int(number, 3)