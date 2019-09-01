# 백준 알고리즘 1931번 문제

def maxCount(list_i) :
    max = 0
    before_e = 0

    for t in list_i :
        start = t[0]
        end = t[1]
        
        if start >= before_e :
            before_e = end
            max += 1
    
    return max

n = int(input())

list_i = []

for i in range(0, n) :
    start, end = map(int, input().split())
    list_i.append((start, end))

list_i.sort(key = lambda element : element[0])

list_i.sort(key = lambda element : element[1])

print(maxCount(list_i))