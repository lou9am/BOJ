# 6198 : 옥상 정원 꾸미기
"""
6.3.토.2023
오큰수랑 같은데 대신 오큰수까지의 개수를 세는 문제
"""
import sys
input = sys.stdin.readline

n = int(input())
stack = []
result = 0
buildings = []

for _ in range(n):
    buildings.append(int(input()))

for i in range(n):
    while stack:
        if (buildings[i] >= stack[-1]):
            stack.pop()
        else:
            result += len(stack)
            break
    stack.append(buildings[i])

print(result)