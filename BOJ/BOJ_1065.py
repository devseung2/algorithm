# 백준 알고리즘 1065 번 문제

N = int(input())

sum = 0

for i in range(1, N+1) :
    N_list = []

    for j in str(i) :
        N_list.append(int(j))

    # 한자리인 경우
    if i < 10 :
        sum += 1
    #  두자리 이상인 경우
    else :
        d = N_list[1] - N_list[0]
        check = True  # 등차수열인지 확인
        
        for j in range(1, len(N_list)) : 
            if N_list[j] - N_list[j-1] != d :
                check = False

        if check :
            sum += 1

print(sum)