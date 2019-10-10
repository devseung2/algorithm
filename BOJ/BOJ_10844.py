# 백준 10844번 문제
N = int(input())

arr = [1 for _ in range(10)]
arr[0] = 0

for i in range(N-1) :
    temp = [0 for _ in range(10)]
    for j in range(10) :
        if 0 <= j < 9:
            temp[j+1] += arr[j]
        if 0 < j <= 9 :
            temp[j-1] += arr[j]
    arr = temp
    
print(sum(arr) % 1000000000)