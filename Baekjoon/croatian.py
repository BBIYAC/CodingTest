# 크로아티아 알파벳
import sys
input = sys.stdin.readline().rstrip()
count = 0
for croatian in ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']:
    if croatian in input:
        # 크로아티아 알파벳의 길이를 1로 보기위해 replace
        input = input.replace(croatian, '_')
print(len(input))