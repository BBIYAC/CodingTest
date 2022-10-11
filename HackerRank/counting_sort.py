# [해커랭크] Counting Sort 1
def countingSort(arr):
    result = [0]*100
    for num in arr:
        result[num] += 1
    return result