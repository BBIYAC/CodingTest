# [코딜리티] Frog Jmp

def solution(X, Y, D):
    div, mod = divmod(Y-X, D)
    if mod == 0:
        return div
    else:
        return div + 1

print(solution(1, 5, 2))