# 2583 영역 구하기
import sys
sys.setrecursionlimit(10**6)

m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]

visited = [[0] * n for _ in range(m)]
area = 1

for _ in range(k):
    lx, ly, rx, ry = map(int, input().split())
    # 직사각형 영역을 1로 변경
    for i in range(m - ry, m - ly, 1): # 문제에서 0, 0이 왼쪽 아래부터 시작하기 때문에 y 좌표를 맞춰준다.
        for j in range(lx, rx, 1):
            graph[i][j] = 1

def dfs(x, y):
    # 그래프 범위 벗어나면
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    # 0이면
    if graph[x][y] == 0:
        # 해당 노드 방문처리
        graph[x][y] = 1
        visited[x][y] = area
        # 상, 하, 좌, 우 재귀호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

area_num = 0
for i in range(m):
    for j in range(n):
        if dfs(i, j) == True:
            area_num += 1
            area += 1
print(area_num)

count = []
for k in range(1, area_num+1):
    cnt = 0
    for i in range(m):
        cnt += visited[i].count(k)
    count.append(cnt)
count.sort()
print(*count, sep=' ')