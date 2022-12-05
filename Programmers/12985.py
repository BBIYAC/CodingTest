# [프로그래머스] 예상 대진표
def solution(n,a,b):
  answer = 1

  while n > 1:
      if (min(a, b) % 2 != 0) and ((a+1 == b) or (a == b+1)):
          break
      answer += 1
      n //= 2
      a = (a+1) // 2
      b = (b+1) // 2

  return answer

print(solution(8, 5, 4)) # 3
