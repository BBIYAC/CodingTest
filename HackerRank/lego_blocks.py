# [해커랭크] Lego Blocks
'''
입력
4
2 2
3 2
2 3
4 4

출력
3
7
9
3375
'''
def legoBlocks(n, m):
    A = 1000000000 + 7
    r = [0]*(m+1)
    a = [0]*(m+1)
    r[1], a[0] = 1, 1

    for j in range(1, m+1):
        a[j] += a[j-1] if j-1>=0 else 0
        a[j] += a[j-2] if j-2>=0 else 0
        a[j] += a[j-3] if j-3>=0 else 0
        a[j] += a[j-4] if j-4>=0 else 0

    for j in range(1, m+1):
        a[j] = a[j] % A
        a[j] = a[j] ** n
        a[j] = a[j] % A
 
    for j in range(2, m+1):
        r[j] = a[j]
        for k in range(1, j):
            r[j] -= r[k]*a[j-k]
        r[j] = r[j] % A
    return r[m] % A

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(legoBlocks(n, m))