# [해커랭크] Flipping the Matrix
def solution(matrix):
    max_sum = 0
    for i in range(len(matrix)//2):
        for j in range(len(matrix)//2):
            max_sum += max(matrix[i][j], matrix[i][-j-1], matrix[-i-1][-j-1], matrix[-i-1][j])
    return max_sum


print(solution([[1, 2], [3, 4]]))