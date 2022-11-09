# [프로그래머스] 성격 유형 검사하기
def solution(survey, choices):
    answer = ''
    personality = {
        'R': 0,
        'T': 0,
        'C': 0,
        'F': 0,
        'J': 0,
        'M': 0,
        'A': 0,
        'N': 0
    }
    
    for i in range(len(choices)):
        if choices[i] < 4:
            personality[survey[i][0]] += 4 - choices[i]
        elif choices[i] > 4:
            personality[survey[i][1]] += choices[i] - 4
            
    answer += 'R' if personality['R'] >= personality['T'] else 'T'
    answer += 'C' if personality['C'] >= personality['F'] else 'F'
    answer += 'J' if personality['J'] >= personality['M'] else 'M'
    answer += 'A' if personality['A'] >= personality['N'] else 'N'
    
    return answer