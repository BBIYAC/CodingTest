# [프로그래머스] 피로도
from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for permu in permutations(dungeons, len(dungeons)):
        temp_k = k
        count = 0
        for [limit, decrease] in permu:
            if temp_k >= limit:
                temp_k -= decrease
                count += 1
        answer = max(answer, count)
    return answer

print(solution(80, [[80,20],[50,40],[30,10]])) # 3