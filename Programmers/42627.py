# [프로그래머스 42627] 디스크 컨트롤러
import heapq
def solution(jobs): 
    answer, current, idx = 0, 0, 0
    start = -1
    heap = []
    
    while idx < len(jobs):
        for job in jobs:
            if start < job[0] <= current:
                heapq.heappush(heap, (job[1], job[0]))
        
        if heap:
            next = heapq.heappop(heap)
            start = current
            current += next[0]
            answer += current - next[1]
            idx += 1
        else:
            current += 1
    return answer // idx