# [코딜리티] Perm Check
def solution1(A):
    max_A = 0
    len_A = 0
    for num in set(A):
        max_A = max(max_A, num)
        len_A += 1
    if max_A == len_A and len(A) == len_A:
        return 1
    else:
        return 0

def solution2(A):
    i = 1
    for num in sorted(A):
        if num != i:
            return 0
        else:
            i += 1
    return 1

print(solution1([9, 5, 7, 3, 2, 7, 3, 1, 10, 8]))
print(solution2([1, 1]))