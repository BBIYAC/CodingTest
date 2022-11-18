# [프로그래머스] 특이한 정렬
def solution(numlist, n):
    return sorted(numlist, key = lambda num: (abs(n-num), -num))