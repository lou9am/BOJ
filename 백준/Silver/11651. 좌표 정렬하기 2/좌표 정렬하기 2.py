n = int(input())

coord = []
for _ in range(n):
    x, y = map(int, input().split())
    coord.append((y, x))

coord.sort()

for c in coord:
    y, x = c
    print(x, y)