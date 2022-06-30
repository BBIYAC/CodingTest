def solution(numbers):
    answer = 0
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for num in array:
        if not num in numbers:
            answer += num
    return answer