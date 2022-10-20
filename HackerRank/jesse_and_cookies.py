# [해커랭크] Jesse and Cookies
import heapq
def cookies(k, A):
    count = 0
    heapq.heapify(A)
    while True:
        if len(A) == 1 and A[0] < k:
            return -1
        if A[0] >= k:
            break
        first, second = heapq.heappop(A), heapq.heappop(A)
        new_num = first + (2*second)
        heapq.heappush(A, new_num)
        count += 1
    return count

n, k = map(int, input().split())
A = list(map(int, input().split()))
print(cookies(k, A))