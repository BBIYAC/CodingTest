# [해커랭크] mini-max sum
def miniMaxSum(arr):
    # Write your code here
    arr = sorted(arr)
    min_sum = sum(arr[:4])
    max_sum = sum(arr[1:])
    print(min_sum, max_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
