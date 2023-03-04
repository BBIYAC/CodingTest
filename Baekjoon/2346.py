# [백준 2346] 풍선 터뜨리기

N = int(input())
s = list(map(int, input().split()))

start = 0
index = [x for x in range(1, N+1)]
answer = []
tmp = s.pop(start)
answer.append(index.pop(start))

while s:
    start = (start + tmp) % len(s) if tmp < 0 else (start + tmp - 1) % len(s)
    tmp = s.pop(start)
    answer.append(index.pop(start))

print(*answer)