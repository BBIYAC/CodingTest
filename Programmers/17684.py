# [프로그래머스] 3차 압축
def solution(msg):
    answer = []
    dic_alpha = {chr(i):i-64 for i in range(65, 91)}
    idx = 27
    start, end = 0, 1

    while end < len(msg) + 1:
        word = msg[start:end]
        if word in dic_alpha:
            end += 1
        else:
            answer.append(dic_alpha[word[:-1]])
            dic_alpha[word] = idx
            idx += 1
            start = end - 1
    answer.append(dic_alpha[word])
    return answer

print(solution('KAKAO'))