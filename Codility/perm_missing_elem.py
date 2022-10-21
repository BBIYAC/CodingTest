# [코딜리티] Perm Missing Elem
def solution(A):
    for i, num in enumerate(sorted(A), start=1):
        if i != num:
            return i
    return len(A)+1