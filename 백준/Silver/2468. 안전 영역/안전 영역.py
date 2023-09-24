# 2468 안전 영역
import sys
sys.setrecursionlimit(10 ** 6) # 메모리 초과
n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# min = min(map(min, graph))
max = max(map(max, graph))

def dfs(map, x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if map[x][y] == 1:
        map[x][y] = 0
        dfs(map, x-1, y)
        dfs(map, x, y-1)
        dfs(map, x+1, y)
        dfs(map, x, y+1)
        return True
    return False

result = 0
for height in range(max):
    count = 0
    # 강수량(높이)에 따라 지도 0,1 처리
    tmp_graph = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > height:
                tmp_graph[i][j] = 1 # 안전하면 1
    
    # 안전지대 개수 카운팅
    for i in range(n):
        for j in range(n):
            if dfs(tmp_graph, i, j) == True:
                count += 1

    if count >= result:
        result = count
print(result)