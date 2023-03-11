# [백준 3029] 경고

import sys
input = sys.stdin.readline

h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

time1 = (h1 * 3600) + (m1 * 60) + s1
time2 = (h2 * 3600) + (m2 * 60) + s2
time = time2 - time1
time += 0 if time2 > time1 else 24 * 60 * 60
hh = time // 3600
mm = time // 60 % 60
ss = time % 60
print("%02d:%02d:%02d" % (hh, mm, ss))