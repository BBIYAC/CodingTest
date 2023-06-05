# [프로그래머스 155651] 호텔 대실
from heapq import heappop, heappush

def solution(book_time):
    answer = 1
    
    times = [(int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:])) for s, e in book_time]
    times.sort()
    
    heap = []
    for s, e in times:
        if not heap:
            heappush(heap,e)
            continue
        if heap[0] <= s:
            heappop(heap)
        else:
            answer += 1
        heappush(heap,e+10)
    
    return answer