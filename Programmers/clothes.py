# 스파이 위장
# def solution(clothes):
#     answer = 0
#     dic = {}
#     # 하나씩 선택하는 경우
#     for c in clothes:
#         if c[1] in dic: 
#             dic[c[1]].append(c[0])
#         else:
#             dic[c[1]] = [c[0]]
#         answer += 1
#     # 조합 개수
#     if len(dic) > 1:
#         count = 1
#         for arr in dic:
#             count *= len(dic[arr])
#         answer += count
    
#     return answer

from collections import Counter

def solution(clothes):
    answer = 1
    c = Counter([x[1] for x in clothes])
    for v in c.values():
        answer *= (v+1)
    answer -= 1
    return answer