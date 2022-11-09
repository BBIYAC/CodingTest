# [프로그래머스] 숫자 짝꿍
def solution(X, Y):
    x_dict = {num: X.count(num) for num in set(X)}
    includes = []

    for y_num in Y:
        if y_num in x_dict and x_dict[y_num] != 0:
            includes.append(y_num)
            x_dict[y_num] -= 1

    result = sorted(includes, reverse=True)
    if not includes:
        return '-1' 
    elif result[0] == '0':
        return '0'
    else:
        return ''.join(result)

print(solution("100", "2345")) # "-1"
# print(solution("10", "1234500")) # "10"