# [해커랭크] Tower Breakers
def towerBreakers():
    answer = []
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        # n: the number of towers, m: the height of each tower
        if n % 2 == 0 or m == 1:
            answer.append(2)
        else:
            answer.append(1)
    print(*answer)


towerBreakers()

