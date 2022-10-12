# [해커랭크] Zig-Zag Sequence
def findZigZagSequence(a, n):
    a.sort()
    mid = int(n/2) # change 1: int((n+1)/2) => int(n/2)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2 # change 2: n - 1 => n - 2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1 # change 3: ed + 1 => ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return