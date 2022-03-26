'''
성적이 낮은 순서로 학생 출력하기
N명의 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름 출력

# 입력 조건
1. 첫 번째 줄에 학생 수 N 입력
2. N+1번째 줄에는 하갯ㅇ의 이름을 나타내는 문자열 A와 학생의 성적을 나타내는 정수 B가 공백으로 구분

# 출력 조건
모든 학생의 이름을 성적이 낮은 순서대로 출력

# 입력 예시
2
홍길동 95
이순신 77

# 출력 예시
이순신 홍길동
'''

## 딕셔너리 사용
dict_n = int(input('>> '))
grade_dict = {}
for i in range(dict_n):
    name, grade = input('>> ').split()
    grade_dict[name] = grade

def dict_solution(grade_dict):
    answer = ''
    sorted_dict = dict(sorted(grade_dict.items(), key=lambda x:x[1]))
    for n_key in sorted_dict.keys():
        answer += n_key+' '
    return answer

print(dict_solution(grade_dict))

## 튜플 사용
n = int(input('>> '))
array = []
for i in range(n):
    input_data = input('>> ').split()
    array.append((input_data[0], int(input_data[1])))

def tuple_solution(array):
    answer = ''
    sorted_array = sorted(array, key=lambda grade:grade[1])
    for student in sorted_array:
        answer += student[0]+' '
    return answer

print(tuple_solution(array))