# [프로그래머스 178870] 연속된 부분 수열의 합
def solution(sequence, k):
    answers = []
    sum = 0
    start = 0
    end = -1
    
    while True:
        if sum < k:
            end += 1
            if end >= len(sequence):
                break
            sum += sequence[end]
        else:
            sum -= sequence[start]
            if start >= len(sequence):
                break
            start += 1
        if sum == k:
            answers.append([start, end])
    
    answers.sort(key=lambda x: (x[1]-x[0], x[0]))
    return answers[0]