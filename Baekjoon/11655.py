# [백준 11655] ROT13
import sys
string = sys.stdin.readline().rstrip()

def ROT13(word):
    ascii = ord(word)
    if 65 <= ascii <= 90:
        if (ascii + 13) > 90:
            ascii = 65 + (ascii + 13 - 90) - 1
        else:
            ascii += 13
    elif 97 <= ascii <= 122:
        if (ascii + 13) > 122:
            ascii = 97 + (ascii + 13 - 122) - 1
        else:
            ascii += 13
    return chr(ascii)
    
result = ''
for s in string:
    result += ROT13(s)
    
print(result)