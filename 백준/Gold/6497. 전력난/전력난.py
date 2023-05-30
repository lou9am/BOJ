# 최소 신장 트리 : 전력난
# 최소 신장 트리 : 우주선과의 교감
import sys
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

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    parent = [i for i in range(m)]

    edges = []
    mst = 0
    full = 0

    for _ in range(n):
        x, y, z = map(int, input().split())
        edges.append((z, x, y))
        full += z

    edges.sort()

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            mst += cost

    print(full - mst)