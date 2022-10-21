# [코딜리티] Max Counters.
def solution(N, A):
    counter = [0]*N
    max_num = 0
    save_max = 0
    for num in A:
        if num <= N:
            if counter[num-1] < save_max:
                counter[num-1] = save_max
            counter[num-1] += 1
            max_num = max(max_num, counter[num-1])
        else:
            save_max = max_num

    for i in range(N):
        if counter[i] < save_max:
            counter[i] = save_max
    return counter

print(solution(5, [3, 4, 4, 6, 1, 4, 4]))

