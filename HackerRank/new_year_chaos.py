# [해커랭크] New Year Chaos
def minimumBribes(q):
    total = 0
    mins = (1e9, 1e9)
    for i, p in list(enumerate(q, 1))[::-1]:
        if p - i > 2:
            total = 0
            break
        elif p > mins[1]:
            total += 2
        elif p > mins[0]:
            total += 1
        if p < mins[0]:
            mins = (p, mins[0])
        elif p < mins[1]:
            mins = (mins[0], p)
    print(total if total else 'Too chaotic')