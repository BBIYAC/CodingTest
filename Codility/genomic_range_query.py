# [코딜리티] Genomic Range Query
# def find_min_value(DNArange):
#     if 'A' in DNArange:
#       return 1
#     elif 'C' in DNArange:
#       return 2
#     elif 'G' in DNArange:
#       return 3
#     elif 'T' in DNArange:
#       return 4

# def solution(S, P, Q):
#     answer = []
#     for i in range(len(P)):
#         answer.append(find_min_value(S[P[i]:Q[i]+1]))
#     return answer

def solution(S, P, Q):
    count = []
    for i in range(3):
        count.append([0]*(len(S)+1))

    for index, DNA in enumerate(S):
        count[0][index+1] = count[0][index] + ( DNA =='A')
        count[1][index+1] = count[1][index] + ( DNA =='C')
        count[2][index+1] = count[2][index] + ( DNA =='G')

    result = []
    for i in range(len(P)):
      start = P[i]
      end = Q[i]+1

      if count[0][end] - count[0][start]:
          result.append(1)
      elif count[1][end] - count[1][start]:
          result.append(2)
      elif count[2][end] - count[2][start]:
          result.append(3)
      else:
          result.append(4)

    return result
    
print(solution('CAGCCTA', [2, 5, 0], [4, 5, 6]))