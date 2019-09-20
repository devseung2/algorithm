# 백준 1436번 문제
import sys

N = int(sys.stdin.readline().strip())
num = 665
while N :
    num += 1
    if str(num).count('666') >= 1 :
        N -= 1
        
print(num)