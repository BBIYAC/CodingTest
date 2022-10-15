# [해커랭크] Truck Tour
def truckTour(petrolpumps):
    remain = 0
    start = 0
    for i, pumps in enumerate(petrolpumps):
        petrol, distance = pumps
        remain += petrol - distance
        # 가솔린 남은 양이 음수인 경우 갱신(마지막으로 음수인 경우 + 1이 시작점)
        if remain < 0:
            start = i + 1
            remain = 0
    return start