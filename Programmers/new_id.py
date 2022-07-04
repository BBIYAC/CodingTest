# 신규 아이디 추천
def solution(new_id):
    answer = ''
    # 1단계 : 소문자로 치환
    id = new_id.lower()
    
    istrue = False
    for i, c in enumerate(id):
        # 2단계 : 소문자, 숫자, 빼기, 밑줄, 마침표를 제외한 모든 문자 제거
        if c.isalpha() or c.isdigit() or c=='-' or c=='_' or c=='.':
            # 3단계 : 마침표가 2번 이상 연속된 부분을 하나의 마침표로 치환
            if not istrue and c=='.':
                istrue = True
            elif istrue and c=='.':
                continue
            else:
                istrue = False
            answer += c
    # 4단계 : 마침표가 처음이나 끝에 위치한다면 제거
    answer = answer.lstrip('.').rstrip('.')
    # 5단계 : 빈 문자열이라면 a 대입
    if answer == '':
        answer = 'a'
    # 6단계 : 길이가 16자 이상이면 15개 문자를 제외한 나머지 문자 제거
    if len(answer) >= 16:
        answer = answer[:15]
    # 나머지 문자 제거 후 마침표가 끝에 위치하면 제거
    if answer[-1] == '.':
        answer = answer[:-1]
    # 7단계 : 길이가 2자 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복
    if len(answer) <= 2:
        for _ in range(3-len(answer)):
            answer += answer[-1]
    return answer