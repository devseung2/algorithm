# 백준 1138번 문제

import sys

N = int(sys.stdin.readline().strip())
arr = [0 for i in range(N)]
_list = list(map(int, sys.stdin.readline().strip().split()))
for i in range(N) :
    count = 0
    for j in range(N) :
        if arr[j] != 0 :
            continue
        elif arr[j] == 0 and count < _list[i] :
            count += 1
        elif count == _list[i] :
            arr[j] = i+1
            break
_str = ""
for i in range(N) :
    _str += str(arr[i]) + " "
print(_str)