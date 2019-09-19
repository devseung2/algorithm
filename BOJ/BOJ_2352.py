# 백준 2352 문제
import sys
import bisect

n = int(sys.stdin.readline().strip())

arr = []

_list = list(map(int, sys.stdin.readline().strip().split()))

for i in range(0, len(_list)) : 
    arr.append(_list[i])
result = [arr[0]]

for i in range(1, n) :
    if result[len(result)-1] < arr[i] :
        result.append(arr[i])
    else : 
        # 이진탐색 알고리즘 (해당 값이 몇 번째 들어가는지 확인)
        idx = bisect.bisect_left(result, arr[i])
        result[idx] = arr[i]

print(len(result))