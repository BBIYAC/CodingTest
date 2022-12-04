# [프로그래머스] N개의 최소공배수
def solution(arr):
    arr.sort(reverse=True)
    answer = arr[0]
    i = 2
    while True:
        isLCM = True
        for num in arr[1:]:
            if answer % num != 0:
                answer = arr[0] * i
                i += 1
                isLCM = False
                break
        if isLCM:
            break
            
    return answer