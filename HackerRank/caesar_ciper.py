# [해커랭크] Caesar Ciper
def caesarCipher(s, k):
    encryption = ''
    for c in s:
        if ord('A') <= ord(c) <= ord('Z'):
            if ord(c)+(k%26) > ord('Z'):
                encryption += chr(ord(c)+(k%26)-26)
            else:
                encryption += chr(ord(c)+(k%26))
        elif ord('a') <= ord(c) <= ord('z'):
            if ord(c)+(k%26) > ord('z'):
                encryption += chr(ord(c)+(k%26)-26)
            else:
                encryption += chr(ord(c)+(k%26))
        else:
            encryption += c
    return encryption