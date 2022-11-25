# [프로그래머스] 아이스 아메리카노
def solution(money):
    div, mod = divmod(money, 5500)
    answer = [div, mod]
    return answer