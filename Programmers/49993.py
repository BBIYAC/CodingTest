# [프로그래머스] 스킬트리
def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        check = []
        for s in tree:
            if s in skill:
                check.append(s)
        if ''.join(check) == skill[:len(check)]:
            answer += 1
    return answer