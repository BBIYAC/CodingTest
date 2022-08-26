# 접미사 배열
import sys
string = sys.stdin.readline().rstrip()
string_len = len(string)
suffix_arr = ['']*string_len
for i in range(string_len):
    suffix_arr[i] = string[i:]
for s in sorted(suffix_arr):
    print(s)