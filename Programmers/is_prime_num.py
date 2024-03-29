import math

# 소수찾기
import math

def is_prime_num(n):
    arr = [True] * (n + 1)
    arr[0] = False
    arr[1] = False

    for i in range(2, int(math.sqrt(n) + 1)):
        if arr[i]:
            j = 2
            while (i * j) <= n:
                arr[i * j] = False
                j += 1

    return arr

arr = is_prime_num(50)
count = 0
for i in range(len(arr)):
    if arr[i]:
        print(i, end=' ')
        count += 1

print(count)