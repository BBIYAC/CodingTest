# [프로그래머스] 모음사전
from itertools import product

def solution(word):
    dictionary = []
    
    for i in range(1, 6):
        for perm in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            dictionary.append(''.join(perm))
            
    return sorted(dictionary).index(word) + 1

print(solution("AAAAE")) # 6