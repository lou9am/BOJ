# 탑
"""
6.2.금.2023
첫 트라이 : 10% 시간 초과
"""
import sys
input = sys.stdin.readline

n = int(input())
tower = list(map(int, input().split()))
stack = []
result = [0] * (n)

for idx, t in enumerate(tower):
    while stack and stack[-1][1] < t:
        stack.pop()
    
    if stack:
        result[idx] = stack[-1][0]
    
    stack.append((idx + 1, t))
        
print(' '.join(map(str, result)))