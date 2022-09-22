# [프로그래머스] 신고 결과 받기

def solution(id_list, report, k):
    answer = []
    # 유저: 신고한 ID
    reported_data = {id:set() for id in id_list}
    # 유저: 정지 메일 수
    reported_count = {id:0 for id in id_list}

    for data in report:
        # 유저 ID, 신고한 ID
        ui, ri = data.split()
        # 중복 없이 유저별 신고 받은 정보 기록
        reported_data[ri].add(ui)

    for ri in id_list:
        # 신고받은 횟수가 k번 이상이고
        if len(reported_data[ri]) >= k:
            for ui in id_list:
                # 유저가 신고한 ID일 경우 카운트
                if ui in reported_data[ri]:
                    reported_count[ui] += 1

    # 정답 리스트에 순서대로 추가
    for id in id_list:
        answer.append(reported_count[id])

    return answer

def solution2(id_list, report, k):
    answer = [0]*len(id_list)
    reports = {user:0 for user in id_list}
    report = set(report)

    for r in report:
        reports[r.split()[1]] += 1

    for r in report:
        ui, ri = r.split()
        if reports[ri] >= k:
            answer[id_list.list(ui)] += 1
    
    return answer
