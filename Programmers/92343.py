# [프로그래머스] 양과 늑대

def solution(info, edges):
    answer = [0]
    graph = {i:[] for i in range(len(info))}
    for parent, child in edges:
        graph[parent].append(child)

    def dfs(currentNode, sheep, wolf, nextNode):
        if info[currentNode] == 0:
            sheep += 1
            answer[0] = max(answer[0], sheep)
        else:
            wolf += 1
        if wolf >= sheep:
            return
        else:
            nextNode.extend(graph[currentNode])
            for node in nextNode:
                dfs(node, sheep, wolf, [n for n in nextNode if n != node])

    dfs(0, 0, 0, [])
    return answer[0]