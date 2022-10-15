# [해커랭크] Recursive Digit Sum
# def digit_sum(n):
#     return sum((int(num) for num in n))

# def superDigit(n, k):
#     s = n * k 
#     if len(s) < 2:
#         return s
#     else:
#         return superDigit(str(digit_sum(n)*k), 1)

# 함수를 분리하면 처리속도가 더 빨라짐
def superDigit(n, k):
    return recursiveDigit(str(digit_sum(n)*k))

def recursiveDigit(n):
    if len(n) < 2:
        return n
    else:
        return recursiveDigit(str(digit_sum(n)))

def digit_sum(n):
    return sum((int(num) for num in n))

print(superDigit('9875', 4))