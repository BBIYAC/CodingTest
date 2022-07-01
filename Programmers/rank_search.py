# 순위 검색
# 정확도 통과, 효율성 미통과
# def solution(info, query):
#     answer = []
    
#     for q in query:
#         question = q.replace(' and', '').split()
#         count = 0
#         for datas in info:
#             data = datas.split()
#             boolean = 0
#             for i in range(4):
#                 if question[i] == data[i] or question[i] == '-':
#                     boolean += 1
#             if boolean == 4 and int(data[4]) >= int(question[4]):
#                 count += 1
                
#         answer.append(count)
            
#     return answer

# 효율성 통과 - 딕셔너리, 이진 탐색법 사용
from itertools import combinations
from collections import defaultdict
import bisect
def solution(info, query):
    answer = []
    people = defaultdict(list)
    for i in info:
        person = i.split()
        score = int(person[-1])
        people[''.join(person[:-1])].append(score)
        for j in range(4):
            candi = list(combinations(person[:-1], j))
            for c in candi:
                people[''.join(c)].append(score)
    for i in people:
        people[i].sort() # 이진 탐색을 사용하기 위한 정렬 
    for i in query:
        key = i.split()
        score = int(key.pop())
        key = ''.join(key)
        key = key.replace('and', '').replace(' ', '').replace('-', '')
        answer.append(len(people[key])-bisect.bisect_left(people[key], score))
    return answer