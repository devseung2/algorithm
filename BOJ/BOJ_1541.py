# 백준 알고리즘 1541 번 문제
import sys

text = sys.stdin.readline().strip().split('-')
_min = 0

if '+' in text[0] : 
    temp = text[0].split('+')
    for v in temp :
        _min += int(v)
else : 
    _min += int(text[0])

for i in range(1, len(text)) : 
    if '+' in text[i] :
        temp = text[i].split('+')
        for v in temp :
            _min -= int(v)
    else :
        _min -= int(text[i])

print(_min)
