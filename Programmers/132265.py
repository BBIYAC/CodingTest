# [프로그래머스 132265] 롤케이크 자르기
from collections import Counter

def solution(topping):
    dic = Counter(topping)
    set_dic = set()
    count = 0
    for piece in topping:
        dic[piece] -= 1
        set_dic.add(piece)
        if dic[piece] == 0:
            dic.pop(piece)
        if len(dic) == len(set_dic):
            count += 1
    return count