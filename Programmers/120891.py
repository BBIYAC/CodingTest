# [프로그래머스] 369 게임
def solution(order):
    number = str(order)
    return number.count('3') + number.count('6') + number.count('9')