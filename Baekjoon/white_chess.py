# 하얀 칸
import sys
white = 0
for i in range(8):
    chess = sys.stdin.readline().rstrip()
    for j in range(8):
        if ((i%2 == 0 and j%2 == 0) or (i%2 == 1 and j%2 == 1)) and chess[j] == 'F':
            white += 1
print(white)