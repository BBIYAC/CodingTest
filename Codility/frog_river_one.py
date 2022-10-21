# [코딜리티] Frog River One
def solution(X, A):
    positions = {}
    for s, p in enumerate(A):
        positions[p] = s
        if len(positions) == X:
            return s

    return -1

print(solution(3, [1, 3, 1, 3, 2, 1, 3]))
print(solution(2, [2, 2, 2, 2, 2]))
print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))