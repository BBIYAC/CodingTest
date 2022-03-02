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

