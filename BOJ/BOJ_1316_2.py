# 백준 1316번 문제
import sys

N = int(sys.stdin.readline().strip())

arr = []
for i in range(N) :
    arr.append(sys.stdin.readline().strip())
    
_sum = 0
for _str in arr : 
    check = True
    for i in range(1, len(_str)) :   
        if _str[i] != _str[i-1] :
            if _str[i+1:len(_str)].count(_str[i-1]) > 0 :
                check = False
        if not check :
            break
    if check : 
        _sum += 1

print(_sum)