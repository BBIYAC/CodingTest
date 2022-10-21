def solution(stack1, stack2, stack3):
    new_stack = ""
    while stack1 or stack2 or stack3:
        idx, num = 0, 0
        if stack1 and stack1[-1] > num:
            num = stack1[-1]
            idx = 1
        if stack2 and stack2[-1] > num:
            num = stack2[-1]
            idx = 2
        if stack3 and stack3[-1] > num:
            num = stack3[-1]
            idx = 3
        
        if idx == 1:
            stack1.pop()
        elif idx == 2:
            stack2.pop()
        elif idx == 3:
            stack3.pop()
        new_stack += str(idx)
    return new_stack

print(solution([2, 7], [4, 5], [1]))