# [백준 1339] 단어 수학

''' 시간초과
import sys
import itertools
input = sys.stdin.readline

N = int(input().rstrip()) # 단어의 개수 N
words = [input().rstrip() for _ in range(N)] # N개의 단어
sorted_words = ''.join(sorted(words, key=len, reverse=True))
convert_alpha = list(''.join(dict.fromkeys(sorted_words)))
convert_number = list(range(9, -1, -1)) # 9 ~ 0

# word to number 변환 함수
def convert(convert_dict, word):
    number = [convert_dict[char] for char in word]
    return int(''.join(number))
        
max_result = 0 # 단어 합의 최댓값
sorted_words = sorted(words, key=len, reverse=True)
for perm in itertools.permutations(convert_alpha, len(convert_alpha)):
    convert_dict = {p:str(convert_number[i]) for i, p in enumerate(perm)} # 문자열 to 숫자 변환 딕셔너리
    sum_result = sum(convert(convert_dict, word) for word in words)  # 변환 후 숫자 합
    max_result = max(max_result, sum_result) # 최댓값

print(max_result)
'''

import sys
input = sys.stdin.readline
word_dict = {chr(ord('A')+i):0 for i in range(26)}

N = int(input().rstrip())
for _ in range(N):
    words = input().rstrip()
    for i, word in enumerate(words[::-1]):
        word_dict[word] += 10 ** i

sorted_words = sorted(word_dict.values(), reverse=True)[:10]
print(sum(value*word for value, word in zip(range(9, -1, -1), sorted_words)))