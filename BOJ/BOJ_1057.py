# 백준 1057번 문제

N, K, L = map(int, (input().split()))
count = 0
while K != L :
    K = (K//2) + (K%2)
    L = (L//2) + (L%2)
    count += 1

print(count)