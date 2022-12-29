# [프로그래머스] 한 번만 등장한 문자
def solution(s):
    answer = []
    for word in set(s):
        if s.count(word) == 1:
            answer.append(word)
    return ''.join(sorted(answer))