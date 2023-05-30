# 기본 수학 2 : 소수 구하기
import math

def is_prinme_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

m, n = map(int, input().split())

for i in range(m, n+1):
    if is_prinme_number(i) == True:
        print(i)