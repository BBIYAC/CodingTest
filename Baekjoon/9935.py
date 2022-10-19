# [백준 9935] 문자열 폭발
import sys
input = sys.stdin.readline

s = input().rstrip()
word = input().rstrip()
len_word =len(word)

stack = []
for chr in s:
    stack.append(chr)
    if ''.join(stack[-len_word:]) == word:
        del stack[-len_word:]

print(''.join(stack) if stack else 'FRULA')