# 기본 수학 2 : 소수
import math
from queue import Empty

m = int(input())
n = int(input())

def is_prinme_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

array = []
for i in range(m, n+1):
    if is_prinme_number(i) == True:
        array.append(i)

if not array:
    print(-1)
else:
    print(sum(array))
    print(min(array))