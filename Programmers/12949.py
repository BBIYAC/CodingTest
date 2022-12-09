# [프로그래머스] 행렬의 곱셈
def solution(arr1, arr2):
  answer = []
  for num in arr1:
    row = []
    for i in range(len(arr2[0])):
      value = 0
      for j in range(len(num)):
        value += num[j]*arr2[j][i]
      row.append(value)
    answer.append(row)
          
  return answer