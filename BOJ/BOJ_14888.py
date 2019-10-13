# 백준 14888번 문제
import itertools

N = int(input())
arr = list(map(int, input().split()))
_list = list(map(int, input().split()))
op = ['+','-','*','/']
signs = []
for i in range(len(_list)) :
    if _list[i] != 0 :
        for j in range(_list[i]) :
            signs.append(op[i])

total_sign = set(itertools.permutations(signs, len(signs)))
_max, _min = -1000000000, 1000000000
for t_s in total_sign :
    _sum = arr[0]
    for i in range(1, len(arr)) :
        sign = t_s[i-1]
        if sign == "+" :
            _sum += arr[i]
        elif sign == "-" :
            _sum -= arr[i]
        elif sign == "*" :
            _sum *= arr[i]
        elif sign == "/" :
            _sum = int(_sum/arr[i])
            
    _max = max(_max, _sum)
    _min = min(_min, _sum)

print(_max)
print(_min)