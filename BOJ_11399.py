# -*- coding: utf-8 -*- 
import sys

n = int(input())
p = list(map(int, input().split()))

if n < 1 or n > 1000:
    print("n 범위 밖(종료)")
    sys.exit(1)

if n != len(p) :
    print("n과 p 입력 수가 다름(종료)")
    sys.exit(1)

for num in p :
    if num < 1 or num > 1000 :
        print("p 범위 밖(종료)")
        sys.exit(1)
        
p.sort()

min_p = p

idx = 1
while idx < len(min_p) : 
    min_p[idx] += min_p[idx-1]
    idx += 1

s=0

for val in min_p :
    s += val

print(s)