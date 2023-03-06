# [백준 11279] 최대 힙

import heapq
import sys
input = sys.stdin.readline

N = int(input().rstrip())
heap = []

for i in range(N):
    num = int(input().rstrip())
    if num == 0:
        print(heapq.heappop(heap)[1] if heap else 0)
    else:
        heapq.heappush(heap, (-num, num))