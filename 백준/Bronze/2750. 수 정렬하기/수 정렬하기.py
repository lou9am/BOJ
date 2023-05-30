import sys
input = sys.stdin.readline
n = int(input())

data = []
for _ in range(n):
    num = int(input().rstrip())
    data.append(num)

data.sort()

for d in data:
    print(d)