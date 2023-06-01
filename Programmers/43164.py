# [프로그래머스 43164] 여행 경로
def solution(tickets):
    answer = []
    path = dict()

    for (start, end) in tickets:
        if start in path:
            path[start].append(end)
        else:
            path[start] = [end]
            
    for r in path.keys():
        path[r].sort(reverse = True)

    st = ["ICN"]
    while st:
        top = st[-1]
        if (top not in path) or (not path[top]):
            answer.append(st.pop())
        else:
            st.append(path[top].pop())

    return answer[::-1]