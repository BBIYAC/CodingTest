# 달팽이 숫자
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    snail = [[0]*n for _ in range(n)]

    # 초기 위치 & 회전 방향
    r, c = 0, 0
    dist = 0 
    
    # 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    for i in range(1, n*n+1):
        snail[r][c] = i
        r += dr[dist]
        c += dc[dist]

        if r<0 or c<0 or r>=n or c>=n or snail[r][c] != 0:
            r -= dr[dist]
            c -= dc[dist]
            dist = (dist+1)%4
            r += dr[dist]
            c += dc[dist]

    print("#{}".format(test_case))
    for row in snail:
        print(*row)
    # ///////////////////////////////////////////////////////////////////////////////////