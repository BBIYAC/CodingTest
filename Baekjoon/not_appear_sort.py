# 중복 없이 정렬
import sys
input = sys.stdin.readline

n = int(input().rstrip())
n_arr = sorted(list(set(map(int, input().split()))))

print(*n_arr)
