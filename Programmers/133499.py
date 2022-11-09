# [프로그래머스] 옹알이 (2)
def solution(babbling):
    count = 0
    words = ["aya", "ye", "woo", "ma"]
    
    for bab in babbling:
        word = ''
        prev = ''
        for b in bab:
            word += b
            if word != prev and word in words:
                prev = word
                word = ''              
        if not word:
            count += 1
        
    return count

print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"])) # 2
print(solution(["aya", "yee", "u", "maa"])) # 1