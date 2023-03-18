# [백준 14890] 경사로

N, L = map(int, input().split())
lists = [list(map(int, input().split())) for _ in range(N)]
answer = 0

# 가로
for i in range(N):
    before = lists[i][0]
    cnt = 1
    for j in range(1, N):
        if lists[i][j] == before:
            cnt += 1
            before = lists[i][j]
        elif lists[i][j]-before == 1 and cnt >= 0:
            # 커졌을 때, cnt가 L보다 커야, 반대쪽 경사로를 놓을 수 있기 때문에 아래 조건문 추가
            if cnt >= L:
                cnt = 1
                before = lists[i][j]
            else:
                break
        elif lists[i][j]-before == -1 and cnt >= 0:
            # 작아졌을 때, cnt >= 0이면 경사로 1개 놓을 수 있는 것이므로 일단 cnt 값 초기화
            cnt = - L + 1
            before = lists[i][j]
        else:
            break
    else:
        if cnt >= 0:
            answer += 1
 
# 세로
for j in range(N):
    before = lists[0][j]
    cnt = 1
    for i in range(1, N):
        if lists[i][j] == before:
            cnt += 1
            before = lists[i][j]
        elif lists[i][j]-before == 1 and cnt >= 0:
            # 커졌을 때, cnt가 L보다 커야, 반대쪽 경사로를 놓을 수 있기 때문에 아래 조건문 추가
            if cnt >= L:
                cnt = 1
                before = lists[i][j]
            else:
                break
        elif lists[i][j]-before == -1 and cnt >= 0:
            # 작아졌을 때, cnt >= 0이면 경사로 1개 놓을 수 있는 것이므로 일단 cnt 값 초기화
            cnt = - L + 1
            before = lists[i][j]
        else:
            break
    else:
        if cnt >= 0:
            answer += 1
 
print(answer)