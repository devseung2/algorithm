# 백준 1094번 문제

X = int(input())
L = [64]
while X < sum(L) :
    pop_val = L.pop(L.index(min(L)))
    L.append(pop_val//2)
    if X > sum(L) :
        L.append(pop_val//2)
    
print(len(L))