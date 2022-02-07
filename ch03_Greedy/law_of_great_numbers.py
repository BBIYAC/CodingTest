'''
큰 수의 법칙
다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙.
단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.

입력 조건
1. 첫째 줄에 N, M, K의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
2. 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1이상 10,000이하의 수로 주어진다.
3. 입력으로 주어지는 K는 항상 M보다 작거나 같다.

출력 조건
첫째 줄에 큰 수의 법칙에 따라 더해진 답을 출력한다.

'''
conditions = [5, 8, 6] # 첫째 줄 N, M, K 입력
nums = [2, 4, 5, 4, 6] # 둘째 줄 배열 입력

def solution(conditions, nums):
    answer = 0
    count = 0
    nums.sort(reverse=True) # 내림차순 정렬
    for i in range(conditions[1]):
        if (i!=0) & (i%conditions[2] == 0):
            count += 1
        answer += nums[count]
    return answer

print(solution(conditions, nums)) # 출력 46