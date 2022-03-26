'''
실패율
스테이지에 도달했으나 아직 클리어하지 못한 플레이어 수 / 스테이지에 도달한 플레이어 수
전체 스테이지 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때,
실패율이 높은 스테이지부터 내림차순으로 스테이지 번호가 담겨있는 배열 return

# 입출력 예시 1
N   stages                       result
5   [2, 1, 2, 6, 2, 4, 3, 3]    [3, 4, 2, 1, 5]
4   [4, 4, 4, 4, 4]             [4, 1, 2 ,3]
'''

def solution(n, stages):
    counts = [0 for _ in range(n)]
    failure = {}
    num = len(stages)

    # 스테이지별 도전자 수
    for stage in stages:
        if stage > n:
            continue
        counts[stage-1] += 1
    
    # 스테이지별 실패율
    for stage, count in enumerate(counts):
        failure[stage+1] = count/num
        num -= count

    answer = sorted(failure, key=failure.get, reverse=True)
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))