# [프로그래머스] 영어 끝말잇기
def solution(n, words):
    answer = [0, 0]
    for idx, word in enumerate(words[1:], start=1):
        if (words[idx-1][-1] != word[0]) or (word in words[:idx]):
            answer = [(idx % n) + 1, (idx // n) + 1]
            break

    return answer