# [프로그래머스] JadenCase
def solution(s):
    answer = [];
    for word in s.split(' '):
        if len(word) == 1:
            word = word.upper()
        if len(word) > 1:
            word = word[0].upper() + word[1:].lower()
        answer.append(word)
    return ' '.join(answer)