# [백준 11286] 절댓값 힙

import heapq
import sys
input = sys.stdin.readline

N = int(input().rstrip())
heap = []

for _ in range(N):
    num = int(input().rstrip())
    if not heap and num == 0:
        print(0)
    elif num == 0:
        print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(num), num))