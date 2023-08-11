from collections import deque

n, k = map(int, input().split())

arr = [0] * (100002)
queue = deque([n])

while queue:
    d = queue.popleft()
    if k == d:
        print(arr[d])
        break

    for i in (d - 1, d + 1, d * 2):
        if 0 <= i < 100001 and arr[i] == 0:
            arr[i] = arr[d] + 1
            queue.append(i)