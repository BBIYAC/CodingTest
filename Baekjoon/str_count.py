# 서로 다른 부분의 문자열 개수
'''
문제
문자열 S가 주어졌을 때, S의 서로 다른 부분 문자열의 개수를 구하는 프로그램을 작성하시오.
부분 문자열은 S에서 연속된 일부분을 말하며, 길이가 1보다 크거나 같아야 한다.
예를 들어, ababc의 부분 문자열은 a, b, a, b, c, ab, ba, ab, bc, aba, bab, abc, abab, babc, ababc가 있고, 서로 다른것의 개수는 12개이다.

입력
첫째 줄에 문자열 S가 주어진다. S는 알파벳 소문자로만 이루어져 있고, 길이는 1,000 이하이다.

출력
첫째 줄에 S의 서로 다른 부분 문자열의 개수를 출력한다.

예제 입력
ababc

예제 출력
12
'''
# import sys
# # 채점 서버의 재귀 깊이 늘리는 코드
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# # 문자열 S
# s = input().strip()
# # 부분 문자열
# s_parts = set()
# len_s = len(s)
# adder = s_parts.add

# # 부분 문자열 구하는 함수
# def comb(s, n):
#     if n == len_s:
#         adder(s)
#         return
#     for i in range(len_s-n+1):
#         adder(s[i:i+n])
#     n += 1
#     comb(s, n)

# comb(s, 1)
# print(len(s_parts))

import sys
input = sys.stdin.readline

# 문자열 S
s = input().strip()
# 부분 문자열
s_parts = set()
for i in range(1, len(s)+1):
    for j in range(len(s)-i+1):
        s_parts.add(s[j:j+i])
print(len(s_parts), s_parts)