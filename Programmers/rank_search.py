# 순위 검색
# 정확도 통과, 효율성 미통과
def solution(info, query):
    answer = []
    
    for q in query:
        question = q.replace(' and', '').split()
        count = 0
        for datas in info:
            data = datas.split()
            boolean = 0
            for i in range(4):
                if question[i] == data[i] or question[i] == '-':
                    boolean += 1
            if boolean == 4 and int(data[4]) >= int(question[4]):
                count += 1
                
        answer.append(count)
            
    return answer