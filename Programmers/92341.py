# [프로그래머스] 주차 요금 계산

import math
def solution(fees, records):
    answer = []
    record_car = {}
    # 출입차 기록 번호별로 딕셔너리
    for record in records:
        time, car, status = record.split()
        if car in record_car:
            record_car[car].append(time)
        else:
            record_car[car] = [time]

    # 차량번호 낮은 순으로 계산
    for car in sorted(record_car):
        car = record_car[car]
        total_time = 0
        # 입차, 출차 내역 둘 다 있는 경우
        for i in range(1, len(car), 2):
            out_time = int(car[i][:2])*60 + int(car[i][-2:])
            in_time = int(car[i-1][:2])*60 + int(car[i-1][-2:])
            total_time += out_time-in_time
        # 입차된 후에 출차된 내역이 없는 경우
        if len(car)%2 != 0:
            total_time += 23*60+59 - (int(car[-1][:2])*60 + int(car[-1][-2:]))
        # 요금 정산
        if total_time >= fees[0]:
            pay = fees[1] + math.ceil((total_time - fees[0])/fees[2]) * fees[3]
            answer.append(pay)
        else:
            answer.append(fees[1])

    return answer