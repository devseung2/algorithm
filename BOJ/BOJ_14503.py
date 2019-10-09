# 백준 14503번 문제

N, M = map(int, (input().split()))
r, c, d = map(int, (input().split()))

arr = []
for i in range(N) :
    arr.append(list(map(int, (input().split()))))

stack = [[r,c]]
# 북, 동, 남, 서
dn = [-1, 0, 1, 0]
dm = [0, 1, 0, -1]
# 북, 동, 남, 서
direction = [[3, 2, 1, 0], [0, 3, 2, 1], [1, 0, 3, 2], [2, 1, 0, 3]]

_sum = 0
while stack : 
    s_n, s_m = stack[len(stack)-1]
    if arr[s_n][s_m] == 0 :
        arr[s_n][s_m] = -1
        _sum += 1
    
    check = True
    for i in direction[d] :
        temp_x = s_n + dn[i]
        temp_y = s_m + dm[i]
        if 0 <= temp_x < N and 0 <= temp_y < M and arr[temp_x][temp_y] == 0 :
            stack.append([temp_x,temp_y])
            d = i
            check = False
            break
            
    if check :
        before_n = s_n + (dn[d]*-1)
        before_m = s_m + (dm[d]*-1)
        if 0 <= before_n < N and 0 <= before_m < M and arr[before_n][before_m] != 1 :
            stack.append([before_n,before_m])
        else :
            break
print(_sum)