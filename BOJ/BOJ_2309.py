# 백준 2309번 문제
import sys, itertools

list_all = []
for i in range(9) :
    list_all.append(int(sys.stdin.readline().strip()))

list_result = itertools.combinations(list_all, 7)

arr = []
for result in list_result : 
    _sum = 0
    for num in result :
        _sum += num
        
    if _sum == 100 :
        for num in result :
            arr.append(num)
        break

print(' '.join(map(str, sorted(arr))))