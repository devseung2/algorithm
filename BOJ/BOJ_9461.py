# 백준 9461번 문제

T = int(input())
temp = [0,1,1,1,2,2]
P = [0 for _ in range(101)]
for i in range(1,6) :
    P[i] = temp[i]

for i in range(T) :
    N = int(input())
    for j in range(6, N+1) :
        P[j] = P[j-5] + P[j-1]
    print(P[N])