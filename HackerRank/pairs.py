# [해커랭크] Pairs
def pairs(k, arr):
    arr = sorted(arr)
    len_arr = len(arr)
    count = 0
    start = 0
    end = 1
    while end < len_arr:
        if arr[end] - arr[start] < k:
            end += 1
        elif arr[end] - arr[start] > k:
            start += 1
            end = start + 1
        elif arr[end] - arr[start] == k:
            count += 1
            start += 1
            end += 1
            
    return count
    
print(pairs(1, [1, 2, 3, 4]))
print(pairs(2, [1, 5, 3, 4, 2]))