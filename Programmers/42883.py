# [프로그래머스 42883] 큰 수 만들기
def solution(number, k):
    stack = []
    for i in range(len(number)):
        while stack and k > 0 and stack[-1] < number[i]:
            stack.pop()
            k -= 1
        stack.append(number[i])
    
    # k개의 숫자를 제거하지 못한 경우 처리
    if k > 0:
        stack = stack[:-k]
    
    answer = ''.join(stack)
    return answer
