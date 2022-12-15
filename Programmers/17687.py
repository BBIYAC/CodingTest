# [프로그래머스] 3차 n진수 게임
def convert(num, base):
    arr = "0123456789ABCDEF"
    q, r = divmod(num, base)

    if q == 0:
        return arr[r]
    else:
        return convert(q, base) + arr[r]
    
def solution(n, t, m, p):
    answer = ''
    result = ''
    
    for i in range(m*t):
        result += str(convert(i, n))
        
    while len(answer) < t:
        answer += result[p-1]
        p += m
        
    return answer