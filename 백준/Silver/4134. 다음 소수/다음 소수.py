# 다음 소수
"""
5.30.화.2023
idea : 소수 판별
"""
import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for _ in range(int(input())):
    n = int(input())
    if n == 0 or n == 1 or n == 2:
        print(2)
        continue
    while True:
        if is_prime(n) == True:
            print(n)
            break
        else:
            n += 1