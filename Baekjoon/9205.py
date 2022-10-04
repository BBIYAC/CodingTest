# [백준 9205] 맥주 마시면서 걸어가기
import sys
input = sys.stdin.readline

def bfs(hx, hy):
    q = [(hx, hy)]
    while q:
        cx, cy = q.pop(0)
        if abs(cx - fx) + abs(cy - fy) <= 1000:
            return 'happy'
        for i in range(N):
            if not visited[i]:
                nx, ny = conv[i]
                if abs(cx - nx) + abs(cy - ny) <= 1000:
                    q.append((nx, ny))
                    visited[i] = True
    return 'sad'

# 테스트 케이스
T = int(input().rstrip())
for _ in range(T):
    result = 'sad'
    # 맥주 파는 편의점 개수
    N = int(input().rstrip())
    
    # 상근이네 집, 편의점, 펜타포트 락 페스티벌 좌표
    hx, hy = map(int, input().split())
    conv = [tuple(map(int, input().split())) for _ in range(N)]
    fx, fy = map(int, input().split())
    visited = [False]*N

    print(bfs(hx, hy))