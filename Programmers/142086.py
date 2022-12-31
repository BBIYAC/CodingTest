# [프로그래머스] 가장 가까운 글자
def solution(s):
    answer = []
    dic_words = {}
    for idx, word in enumerate(s):
        if word not in dic_words:
            answer.append(-1)
            dic_words[word] = [idx]
        else:
            answer.append(idx-dic_words[word][-1])
            dic_words[word].append(idx)
    return answer