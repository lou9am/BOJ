t = int(input())

for _ in range(t):
    n = int(input())
    stock = list(map(int, input().split()))

    result, max_stock = 0, 0
    for s in reversed(stock):
        if s > max_stock:
            max_stock = s
        else:
            result += max_stock - s

    print(result)