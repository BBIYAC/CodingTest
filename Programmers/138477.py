# [프로그래머스] 명예의 전당 (1)
from heapq import heappush, heappop

def solution(k, score):
    answer = []
    heap = []
    for day, s in enumerate(score, start=1):
        heappush(heap, s)
        if day > k: heappop(heap)
        answer.append(heap[0])
    return answer