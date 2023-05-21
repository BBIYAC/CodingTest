# [프로그래머스 67258] 보석 쇼핑
def solution(gems):
    N = len(gems)
    answer = [0, N-1]
    kind = len(set(gems)) 
    dic = {gems[0]:1,}
    start, end = 0, 0 
    while start < N and end < N:
        if len(dic) < kind:
            end += 1
            if end == N:
                break
            dic[gems[end]] = dic.get(gems[end], 0) + 1
            
        else:
            if (end-start+1) < (answer[1]-answer[0]+1):
                answer = [start, end]
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            start += 1

    return [answer[0] + 1, answer[1] + 1]