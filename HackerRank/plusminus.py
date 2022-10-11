# [해커랭크] PlusMinus
import sys

def plusMinus(arr):
    rate = [0, 0, 0]
    for num in arr:
        if num > 0: # 양수
            rate[0] += 1
        elif num < 0: # 음수
            rate[1] += 1
        else: # 0
            rate[2] += 1
    for r in rate:
        print("{:6f}".format(r/len(arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)