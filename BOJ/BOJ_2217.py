# 백준 알고리즘 2217번 문제

N = int(input())

k_list = []

for i in range(N) :
    W = int(input())
    k_list.append(W)

k_list.sort(reverse = True)

k_max = [0 for x in range(N)]

for i in range(N) :
    k_max[i] = k_list[i] * (i+1)

print(max(k_max))