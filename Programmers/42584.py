# [프로그래머스] 주식가격
from collections import deque

def solution(prices):
    prices = deque(prices)
    answer = []
    while prices:
        price = prices.popleft()
        count = 0
        for next_price in prices:
            count += 1
            if next_price < price:
                break
        answer.append(count)
    return answer