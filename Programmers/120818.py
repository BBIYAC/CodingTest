# [프로그래머스] 옷가게 할인받기
def solution(price):
    if price >= 500000:
        return int(price * 0.8)
    if price >= 300000:
        return int(price * 0.9)
    if price >= 100000:
        return int(price * 0.95)
    return price