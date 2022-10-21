# [코딜리티] Missing Integer
def solution(A):
    count = [False] * 1000001
    for num in A:
        if num > 0 and not count[num-1]:
            count[num-1] = True
    for num, c in enumerate(count):
        if not c:
            return num + 1

print(solution([1, 2, 3]))