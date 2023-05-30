# [프로그래머스 49189] 가장 먼 노드
def solution(n, edge):
    distance = [[] for _ in range(n + 1)]
    for v1, v2 in edge:
        distance[v1].append(v2)
        distance[v2].append(v1)
    
    visited = [0 for _ in range(n + 1)]
    visited[1] = 1
    
    queue = [1]
    while queue:
        cur = queue.pop(0)
        for dest in distance[cur]:
            if not visited[dest]:
                visited[dest] = visited[cur] + 1
                queue.append(dest)
        
    return visited.count(max(visited))