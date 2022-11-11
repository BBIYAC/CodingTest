# [프로그래머스] 과일 장수
def solution(k, m, score):
    answer = 0
    sortedScore = sorted(score, reverse=True)
    p = k
    for i in range(len(score)):
        p = min(p, sortedScore[i])
        if (i+ 1) % m == 0:
            answer += p * m
            p = k
    return answer