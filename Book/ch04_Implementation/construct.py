'''
기둥과 보 설치
1. 기둥은 바닥 위에 있거나 보의 한 쪽 끝부분 위에 있거나 또는 다른 기둥 위에 있어야 한다.
2. 보는 한쪽 끝부분이 기둥 위에 있거나, 또는 양쪽 끝부분이 다른 보와 동시에 연결되어 있어야 한다.

맨 처음 벽면(바닥)은 비어 있는 상태
기둥과 보는 격자 선의 교차점에 걸치지 않고, 격자 칸의 각 변에 정확히 일치하도록 설치할 수 있다.

# 입출력 예시 1
n: 5
build_frame: [[1,0,0,1], [1,1,1,1], [2,1,0,1], [2,2,1,1], [5,0,0,1], [5,1,0,1], [4,2,1,1], [3,2,1,1]]
result: [[1,0,0], [1,1,1], [2,1,0], [2,2,1], [3,2,1], [4,2,1], [5,0,0], [5,1,0]]

# 입출력 예시 2
n: 5
build_frame: [[0,0,0,1], [2,0,0,1], [4,0,0,1], [0,1,1,1], [1,1,1,1], [2,1,1,1], [3,1,1,1], [2,0,0,0], [1,1,1,0], [2,2,0,1]]
resultt: [[0,0,0], [0,1,1], [1,1,1], [2,1,1], [3,1,1], [4,0,0]]
'''

# 정답

# 현재 설치된 구조물이 '가능한' 구조물인지 확인하는 함수
def possible(answer):
    for x, y, a in answer:
        if a == 0: # 설치된 것이 '기둥'인 경우
            # '바닥 위' 혹은 '보의 한쪽 끝부분 위' 혹은 '다른 기둥 위'라면 정상
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False # 아니라면 거짓
        elif a == 1: # 설치된 것이 '보'인 경우
            # 한쪽 끝부분이 기둥 위' 혹은 '양쪽 끝부분이 다른 보와 동시에 연결'이라면 정상
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True

def answer_solution(n, build_frame):
    answer = []
    for build in build_frame:
        x, y, a, b = build
        if b == 0: # 삭제
            answer.remove([x, y, a])
            if not possible(answer): # 삭제가 불가능하면
                answer.append([x, y, a])
        if b == 1: # 설치
            answer.append([x, y, a])
            if not possible(answer): # 설치가 불가능 하면
                answer.remove([x, y, a])
    return sorted(answer) # 정렬된 결과 반환


# TEST 1
print(answer_solution(5, [[1,0,0,1], [1,1,1,1], [2,1,0,1], [2,2,1,1], [5,0,0,1], [5,1,0,1], [4,2,1,1], [3,2,1,1]]))

# TEST 2
print(answer_solution(5, [[0,0,0,1], [2,0,0,1], [4,0,0,1], [0,1,1,1], [1,1,1,1], [2,1,1,1], [3,1,1,1], [2,0,0,0], [1,1,1,0], [2,2,0,1]]))