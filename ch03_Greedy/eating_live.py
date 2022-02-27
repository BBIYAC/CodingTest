'''
무지의 먹방 라이브
1. 무지는 1번 음식부터 먹기 시작하며, 회전판은 번호가 증가하는 순서대로 음식을 무지 앞으로 가져다 놓는다.
2. 마지막 번호의 음식을 섭취한 후에는 회전판에 의해 다시 1번 음식이 무지 앞으로 온다.
3. 무지는 음식 하나를 1초 동안 섭취한 후 남은 음식은 그대로 두고, 다음 음식을 섭취한다.
   (다음 음식: 남은 음식 중 다음으로 섭취해야 할 가장 가까운 번호의 음식)
4. 회전판이 다음 음식을 무지 앞으로 가져오는 데 걸리는 시간은 없다고 가정한다.

먹방 시작한 지 K초 후에 네트워크 장애로 인해 방송이 잠시 중단되었고, 
다시 방송을 이어갈 때, 몇 번 음식부터 섭취해야 하는지를 알고자 한다.

# 제한 사항
1. food_times는 각 음식을 모두 먹는 데 필요한 시간이 음식의 번호 순서대로 들어 있는 배열
2. k는 방송이 중단된 시간을 나타냄
3. 만약 더 섭취해야 할 음식이 없다면 -1을 반환

# 입출력 예시
food_times : [3, 1, 2]
k : 5
result : 1
'''

def solution(food_times, k):
    times = food_times
    if sum(times) <= k:
        return -1
    
    for i in range(sum(times)):
        eat = i%3
        # 먹을 음식이 없으면 다음 음식
        if times[eat] == 0:
            eat = (i+1)%3
        k -= 1
        times[eat] -= 1
        result = (eat+1)%3+1
        # k번 먹었으면(k초 후)
        if k == 0:
            return result
    # 모든 음식을 다 먹었으면
    return -1

print(solution([3, 1, 2], 5))

# 큐 이용
import heapq

def queue_solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i+1))

    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식의 개수

    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda x: x[1]) # 음식의 번호 기준으로 정렬
    return result[(k-sum_value) % length][1] 

print(queue_solution([3, 1, 2], 5))