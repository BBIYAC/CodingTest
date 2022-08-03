# 조이스틱
def solution(name):
    # 이름 만들기 - A의 아스키 코드 65, Z의 아스키 코드 90(다음 A는 91)
    answer = 0
    for n in name: 
        n_ord = ord(n) # 주어진 문자의 아스키코드
        center = 78 # A 와 다음 A의 가운데 값
        if n_ord > center: # 다음 A와 더 가까운 경우
            answer += 91-n_ord
        else: # 처음 A와 더 가까운 경우
            answer += n_ord-65
    
    # 커서 이동
    if name.find('A') == -1: # A가 없을 때
        return answer + len(name)-1
    else: # A가 있을 때
        # 1. 이동하지 않는 경우(첫 번째 알파벳만 A가 아님 or 모두 A)
        if len(name.rstrip('A')) <= 1:
            return answer
        # 2. 오른쪽으로 쭉 이동하는 경우
        move2 = len(name[1:].rstrip('A'))
        # 3. 오른쪽으로 갔다가 왼쪽으로 이동하는 경우
        move3 = 1e9 # 최소 이동 수
        for i in range(1, len(name)//2):
            move3 = min(move3, 2*(len(name[:i+1])-1) + len(name[i+1:].lstrip('A')))
        # 4. 왼쪽으로 쭉 이동하는 경우
        move4 = len(name[1:].lstrip('A'))
        # 5. 왼쪽으로 갔다가 오른쪽으로 이동하는 경우
        move5 = 1e9 # 최소 이동 수
        for i in range(1, len(name)//2):
            move5 = min(move5, 2*len(name[-i+1:])-1 + len(name[:-i+1].rstrip('A')))
        return answer+min(move2, move3, move4, move5)