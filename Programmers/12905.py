# [프로그래머스] 가장 큰 정사각형
def solution(board):
    answer = 1 if 1 in board[0] or 1 in board[-1] else 0
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
            answer = max(answer, board[i][j])            

    return answer ** 2

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])) # 9
print(solution([[0,0,1,1],[1,1,1,1]])) # 4