# [코딜리티] Binary Gap
def solution(N):
    max_length = 0
    N = str(bin(N))[2:]
    i = 1
    prev = 0
    while i < len(N):
        if N[i] == '1':
            max_length = max(i-prev-1, max_length)
            prev = i
        i += 1
    return 0 if max_length == 0 and N[-1] == '0' else max_length

print(solution(32))