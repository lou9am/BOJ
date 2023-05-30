# 1934 최소공배수
import sys
import math
input = sys.stdin.readline
lst = []

for _ in range(int(input())):
    a, b = map(int, input().split())
    lst.append(math.lcm(a, b)) # 최대공약수를 이용해 최소공배수 계산하여 저장

print('\n'.join(map(str, lst)))