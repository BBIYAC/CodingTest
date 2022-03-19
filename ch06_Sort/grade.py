'''
국영수
N명의 이름과 국어, 영어, 수학 점수가 주어질 때 다음 조건으로 학생의 성적 정렬
1. 국어 점수가 감소하는 순서로
2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로

# 입력 조건
1. 학생수 N
2. 한 줄에 하나씩 각 학생의 이름, 국어, 영어, 수학 점수가 공백으로 구분
3. 점수는 1보다 크거나 같고, 100보다 작거나 같은 자연수
4. 이름은 알파벳 대문자로 이루어진 문자열, 길이는 10자 이내

# 출력조건
문제에 나와있는 정렬 기준으로 정렬 후 첫째 줄부터 N개의 줄에 걸쳐 학생 이름 출력

# 입력 예시
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90

# 출력 예시
Donghyuk
Sangkeun
Sunyoung
nsj
Wonsekb
Sanghyun
Sei
Kangsoo
Haebin
Jumkyu
Soong
Taewhan
'''

def solution():
    answer = ''
    n = int(input('>> '))
    grades = []
    for _ in range(n):
        n, k, e, m = input('>> ').split()
        grades.append({'name': n, 'korean': int(k), 'english': int(e), 'math': int(m)})
    # 정렬 조건에 따른 정렬
    sorted_dict = sorted(grades, key = lambda x : (-x['korean'], x['english'], -x['math'], x['name']))
    for grade in sorted_dict:
        answer += grade['name']+'\n'
    return answer

print(solution())
