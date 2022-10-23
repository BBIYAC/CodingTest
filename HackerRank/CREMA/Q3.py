def maxLength(a, k):
    len_a = len(a)
    longest = 0
    for i in range(1, len_a+1):
        for j in range(len_a-i+1):
            print(a[j:j+i])
            if sum(a[j:j+i]) <= k:
                longest = i
                break
    return longest
print(maxLength([4, 3, 1, 2, 1], 4))