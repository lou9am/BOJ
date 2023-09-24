# 5014 스타링크 (14:30)
from collections import deque

# s에 있는 사람이 총 f인 건물의 g로 가고 싶음
f, s, g, u, d = map(int, input().split())
visited = [False] * (f + 1)

def bfs(start, visited):
    queue = deque([(start, 0)])
    # 현재 위치(층) 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        v, count = queue.popleft()
        if v == g:
            return count    

        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in [u, -d]:
            next = v + i 
            
            # 건물 범위를 벗어나면
            if next <= 0 or next > f:
                continue
            if not visited[next]:
                queue.append((next, count + 1))
                visited[next] = True
    return "use the stairs"

print(bfs(s, visited))