# [프로그래머스] 연속 부분 수열 합의 개수

# solution 1
def solution(elements):
    temp = elements * 2
    answers = []
    elements_len = len(elements)
    for i in range(elements_len):
        for j in range(1, elements_len+1):
            answers.append(sum(temp[i:i+j]))

    return len(set(answers))


# solution 2
def solution(elements):
    temp = elements * 2
    answers = set()
    elements_len = len(elements)
    for i in range(elements_len):
        for j in range(1, elements_len+1):
            answers.add(sum(temp[i:i+j]))

    return len(answers)