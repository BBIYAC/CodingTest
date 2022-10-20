# [해커랭크] Balanced Brackets
def isBalanced(s):
    stack = []
    for chr in s:
        print(stack)
        if chr in '{[(':
            stack.append(chr)
        elif stack and (stack[-1]+chr == '{}' or stack[-1]+chr == '[]' or stack[-1]+chr == '()'):
            stack.pop()
        else:
            return 'NO'

    return 'NO' if stack else 'YES'

print(isBalanced('{(([])[])[]}[]'))