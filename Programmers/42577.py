# [프로그래머스] 전화번호 목록
def solution(phone_book):
    stack = []
    print(sorted(phone_book))
    for phone in sorted(phone_book):
        if not stack:
            stack.append(phone)
            continue
            
        prevPhone = stack.pop()
        if prevPhone == phone[:len(prevPhone)]:
            return False
        stack.append(phone)
    return True

print(solution(["934793", "34", "44", "9347"])) # False