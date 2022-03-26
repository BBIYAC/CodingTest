'''
좌물쇠와 열쇠
열쇠를 나타내는 2차원 배열 key와 자물쇠를 나타내는 2차원 배열 lock이 매개변수로 주어질 때,
열쇠로 자물쇠를 열 수 있으면 true, 열 수 없으면 false를 return

# 입력 key
[[0, 0, 0], 
 [1, 0, 0], 
 [0, 1, 1]]

# 입력 lock
[[1, 1, 1], 
 [1, 1, 0], 
 [1, 0, 1]]

# 출력
true
'''
# 프로그래머스(https://programmers.co.kr/learn/courses/30/lessons/60059?language=python3) 채점 결과 런타임 에러
def solution(key, lock):
    # 구멍
    lock_hole = []
    # 열쇠
    way = []

    # 구멍 위치 파악
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 0:
                lock_hole.append((i, j))
    # 열쇠 위치 파악
    for i in range(len(key)):
        for j in range(len(key)):
            if key[i][j] == 1:
                way.append((i, j))

    # 열쇠 구멍 맞추기
    for i in range(1, len(way)):
        for j in range(i, len(way)):
            if (abs(lock_hole[1][0]-lock_hole[0][0])==abs(way[j][0]-way[i-1][0]) 
                & abs(lock_hole[1][1]-lock_hole[0][1])==abs(way[j][1]-way[i-1][1])):         
                return True
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))


# 정답
# 2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(a):
    n = len(a) # 행 길이 계산
    m = len(a[0]) # 열 길이 계산
    result = [[0]*n for _ in range(m)] # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] != 1:
                return False
    return True

def answer_solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    # 4가지 방향에 대해서 확인
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key) # 열쇠 회전
        for x in range(n*2):
            for y in range(n*2):
                # 자물쇠에 열쇠를 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
                if check(new_lock) == True:
                    return True
                # 자물쇠에서 열쇠를 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False

print(answer_solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))        