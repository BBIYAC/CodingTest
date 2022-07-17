# 단어 공부
'''
문제
알파벳 대소문자로 된 단어가 주어지면, 
이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
단, 대문자와 소문자를 구분하지 않는다.

입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 
단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

예제 입력 1
Mississipi

예제 출력 1
?
'''

import sys
input = sys.stdin.readline().rstrip().upper()

# 같은 문자들끼리 카운트
count = dict()
for s in input:
    if s in count:
        count[s] += 1
    else:
        count[s] = 1

# 값이 하나일 때 True, 여러 개일 때 False
only_one = True 
answer = input[0]
for k, v in count.items():
    if count[answer] < count[k]: # 카운트 수가 최대인 문자 찾기
        answer = k
        only_one = True
    elif count[k] == count[answer]: # 카운트 수가 같은 경우(여러 개)
        only_one = False

# 가장 많이 카운트 된 문자 출력(여러 개면 ? 출력)
print(answer if only_one else '?')