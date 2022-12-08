# [프로그래머스] 1차 캐시
def solution(cacheSize, cities):
  answer = 0
  memolist = []
  
  if cacheSize == 0:
    return len(cities) * 5
  
  for i in range(len(cities)):
    cities[i] = cities[i].upper()
    
    if cities[i] in memolist:
      memolist.remove(cities[i])
      memolist.append(cities[i])
      answer += 1
        
    else:
      answer += 5
      if len(memolist) == cacheSize:
          memolist.pop(0)
      memolist.append(cities[i])
          
  return answer