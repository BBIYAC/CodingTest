# [해커랭크] Grid Challenge
def gridChallenge(grid):
    sorted_grid = [sorted(g) for g in grid]
    for i in range(len(grid[0])):
        check_grid = [g[i] for g in sorted_grid]
        if check_grid != sorted(check_grid):
            return 'NO'
    return 'YES'

N = int(input())
grid = [list(input()) for _ in range(N)]
result = gridChallenge(grid)
print(result)