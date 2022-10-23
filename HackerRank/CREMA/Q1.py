def getFinalString(s):
    len_word = 3 # AWS Length
    stack = []
    for alpha in s:
        stack.append(alpha)
        if ''.join(stack[-len_word:]) == "AWS":
            del stack[-len_word:]
    return ''.join(stack) if stack else "-1"