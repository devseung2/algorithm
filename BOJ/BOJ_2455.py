# 백준 2455번 문제
arr = []
for i in range(4) :
    arr.append(list(map(int, input().split())))

_max, _sum = 0, 0
for _arr in arr :
    _sum += _arr[1] - _arr[0]
    _max = max(_max, _sum)
    
print(_max)