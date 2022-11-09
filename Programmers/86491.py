# [프로그래머스] 최소 직사각형
def solution(sizes):
    width, height = 0, 0
    for [left, right] in sizes:
        if left > right:
            width = max(width, left)
            height = max(height, right)
        else:
            width = max(width, right)
            height = max(height, left)
    return width * height