# 프로그래머스 파괴되지 않은 건물

def solution(board, skill):
    answer = 0
    temp = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]

    for s_type, r1, c1, r2, c2, degree in skill:
        temp[r1][c1] += degree if s_type == 2 else -degree
        temp[r1][c2+1] += -degree if s_type == 2 else degree
        temp[r2+1][c1] += -degree if s_type == 2 else degree
        temp[r2+1][c2+1] += degree if s_type == 2 else -degree

    # 행 기준 누적합
    for i in range(len(temp)-1):
        for j in range(len(temp[0])-1):
            temp[i][j+1] += temp[i][j]

    # 열 기준 누적합
    for j in range(len(temp[0])-1):
        for i in range(len(temp)-1):
            temp[i+1][j]+=temp[i][j]

    # 기존 배열에 적용
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += temp[i][j]
            # board에 값이 1이상인 경우 카운트
            if board[i][j] > 0: answer += 1

    return answer