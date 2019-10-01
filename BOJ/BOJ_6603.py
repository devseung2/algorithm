# 백준 6603번 문제

import sys, itertools

while True :
    _list = list(map(int, sys.stdin.readline().strip().split()))
    k = _list.pop(0)
    lotto = itertools.combinations(_list, 6)

    if k == 0 :
        break
    for nums in lotto :
        print(' '.join(map(str, nums)))
    print()