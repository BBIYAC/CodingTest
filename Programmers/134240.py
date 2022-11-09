# [프로그래머스] 푸드 파이터 대회
def solution(food):
    left = ''
    for calorie, one_food in enumerate(food[1:], start = 1):
        left += str(calorie) * (int(one_food) // 2)
    right = left[::-1]
    return left + '0' + right