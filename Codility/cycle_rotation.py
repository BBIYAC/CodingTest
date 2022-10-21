# [코딜리티] Cycle Rotation
from collections import deque
def solution(A, K):
    queue = deque(A) 
    if not queue:
        return []
    for _ in range(K):
        num = queue.pop()
        queue.insert(0, num)
    return list(queue)

print(solution([], 3))