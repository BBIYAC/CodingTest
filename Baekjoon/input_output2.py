# 그대로 출력하기2
while 1:
    try:
        print(input())
    except EOFError:
        break
