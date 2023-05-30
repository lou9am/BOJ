import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, end):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
            
    return distance[end] - distance[start]

for _ in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    ans = []
    for _ in range(t):
        x = int(input())
        s_to_g = dijkstra(s, g)
        g_to_h = dijkstra(g, h)
        h_to_x = dijkstra(h, x)

        s_to_h = dijkstra(s, h)
        h_to_g = dijkstra(h, g)
        g_to_x = dijkstra(g, x)
        
        if s_to_g + g_to_h + h_to_x == dijkstra(s, x) or s_to_h + h_to_g + g_to_x == dijkstra(s, x):
            ans.append(x)        
        
    ans.sort()
    print(' '.join(map(str,ans)))