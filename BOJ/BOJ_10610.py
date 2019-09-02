# 백준 알고리즘 10610번 문제
import sys
 
N = input()

N_list = []

for i in N :
    N_list.append(i)

N_list.sort(reverse = True)

str_max = "".join(N_list)

if (int(str_max) % 30) == 0 :
    print(str_max)
else :
    print(-1)