T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    array = list(map(int,input().split()))
    sum = 0
    for i in range(2, n-2):
        if (array[i]>max(array[i-1], array[i-2]) and array[i]>max(array[i+1], array[i+2])):
            sum += (array[i]-max(array[i-1], array[i-2], array[i+1], array[i+2]))
    print("#"+str(test_case)+" "+str(sum))
    # ///////////////////////////////////////////////////////////////////////////////////