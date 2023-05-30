# 큐, 덱 : 프린터 큐
from collections import deque

for _ in range(int(input())):
    n, m = map(int, input().split())
    queue = deque(map(int, input().split()))

    cnt = 0
    while queue:
        best = max(queue)
        front = queue.popleft()
        m -= 1

        if best == front:
            cnt += 1
            if m < 0:
                print(cnt)
                break
        else:
            queue.append(front)
            if m < 0 :
                m = len(queue) - 1