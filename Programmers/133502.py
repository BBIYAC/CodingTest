# [프로그래머스] 햄버거 만들기
def solution(ingredient):
    answer = 0
    start = []
    for i in ingredient:
        start.append(i)
        if start[-4:] == [1, 2, 3, 1]:
            answer += 1
            for i in range(4):
                start.pop()
            
    return answer


# solution([2, 1, 1, 2, 3, 1, 2, 3, 1]) # 2
print(solution([1, 1, 2, 1, 2, 3, 1, 3, 1, 2, 3, 1])) # 3