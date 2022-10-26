# [백준 1460] 에디터
'''
slice 시간복잡도 - O(b-a) # 슬라이싱 길이에 비례
append, pop 시간복잡도 - O(1) # 슬라이싱보다 짧음
'''
import sys
input = sys.stdin.readline

stack1 = list(input().rstrip())
stack2 = list()

M = int(input().rstrip())
for _ in range(M):
    inputs = input().split()
    command = inputs[0]
    # 커서 왼쪽으로 한 칸 옮김
    if command == 'L':
        # 커서가 문장의 맨 앞이면 무시됨
        if stack1:
            stack2.append(stack1.pop())
    # 커서 오른쪽으로 한 칸 옮김
    elif command == 'D':
        # 커서가 문장의 맨 뒤이면 무시됨
        if stack2:
            stack1.append(stack2.pop())
    # 커서 왼쪽에 있는 문자를 삭제함
    elif command == 'B':
        # 커서가 문장의 맨 앞이면 무시됨
        if stack1:
            stack1.pop()
    else: # 문자를 커서 왼쪽에 추가함
        stack1.append(inputs[1])

print(''.join(stack1) + ''.join(stack2[::-1]))

# # 입력되어 있는 문자열
# S = input().rstrip()
# # 입력할 명령어 개수
# M = int(input().rstrip())
# # 커서 위치
# cursor = len(S)
# S = "."+(S)
# for i in range(M):
#     inputs = input().split()
#     command = inputs[0]
#     # 커서 왼쪽으로 한 칸 옮김
#     if command == 'L':
#         # 커서가 문장의 맨 앞이면 무시됨
#         if cursor != 0:
#             cursor -= 1
#     # 커서 오른쪽으로 한 칸 옮김
#     elif command == 'D':
#         # 커서가 문장의 맨 뒤이면 무시됨
#         if cursor != len(S):
#             cursor += 1
#     # 커서 왼쪽에 있는 문자를 삭제함
#     elif command == 'B':
#         # 커서가 문장의 맨 앞이면 무시됨
#         if cursor != 0:
#             S = S[:cursor]+S[cursor+1:]
#             cursor -= 1
#     else: # 문자를 커서 왼쪽에 추가함
#         S = S[:cursor+1]+inputs[1]+S[cursor+1:]
#         cursor += 1
    
# print(S[1:])