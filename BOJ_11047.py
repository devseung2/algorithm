# 백준 알고리즘 11047번 문제
# 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
# 둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

import sys

input1 = list(map(int, input().split()))

input_list = []

n = input1[0]
k = input1[1]

if n < 1 or n > 10 :
    print("[err] N 범위 밖")
    sys.exit(1)

if k < 1 or k > 100000000 :
    print("[err] K 범위 밖")
    sys.exit(1)

for i in range(0, n) :
    val = int(input())

    if(i >= 1 and val <= input_list[i-1]) :
        print("입력 숫자를 오름차순으로 입력하세요.")
        sys.exit(1)

    input_list.append(val)

min = 0
idx = len(input_list)-1

while k != 0 :
    if idx < 0 :
        print("N 종류로 나눌 수 없음")
        sys.exit(1)

    num = int(k / input_list[idx])
    k = k % input_list[idx]
    min += num
    idx -= 1

print(min)