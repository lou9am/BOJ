# 17103 골드바흐 파티션
"""
5.39.화.2023
idea : 2부터 n의 제곱근까지 확인하면 됨
"""

import sys
import math
input = sys.stdin.readline

n = 1000000
array = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n))+1):
    if array[i] == True: # i가 남은 수(소수)인 경우
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

for _ in range(int(input())):
    n = int(input()) # 4 이상 짝수
    
    cnt = 0 # 골드바흐 파티션 수
    for i in range(2, n // 2 + 1):
        if array[i] and array[n-i]: # 둘 다 소수면
            cnt += 1

    print(cnt)