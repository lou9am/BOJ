n = int(input())

data = []
for _ in range(n):
    num = int(input())
    data.append(num)

data.sort()

for d in data:
    print(d)