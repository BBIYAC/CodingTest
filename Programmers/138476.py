# [프로그래머스] 귤 고르기
def solution(k, tangerine):
    answer = 0
    sum = 0
    t_dict = {}
    for t in tangerine:
        if t in t_dict:
            t_dict[t] += 1
        else:
            t_dict[t] = 1
    
    for num in sorted(t_dict.values(), reverse=True):
        answer += 1
        sum += num
        if sum >= k:
            break
    
    return answer