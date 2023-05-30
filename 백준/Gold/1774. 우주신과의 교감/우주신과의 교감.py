# 최소 신장 트리 : 우주선과의 교감
import sys
import math
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = dict()

coord = []
for i in range(n):
    x, y = map(float, input().split())
    coord.append((x,y))
    parent[i] = i

for _ in range(m):
    a, b = map(int, input().split())
    if find_parent(parent, a-1) != find_parent(parent, b-1):
        union_parent(parent, a-1, b-1)

edges = []
result = 0

# n개의 좌표마다 간선 비용 계산해 edges에 넣기
for j in range(n):
    for i in range(j+1, n):
        cost = math.sqrt((coord[j][0] - coord[i][0])**2 + (coord[j][1] - coord[i][1])**2)
        edges.append((cost, j, i))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print("{:.2f}".format(result))