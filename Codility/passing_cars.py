# [코딜리티] Passing Cars
def solution(A):
  answer = 0
  east = 0
  for num in A:
    if num == 0:
      east += 1
    else:
      answer += east
  return answer if answer <= 1000000000 else -1

print(solution([0, 1, 0, 1, 1]))