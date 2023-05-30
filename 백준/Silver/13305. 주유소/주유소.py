n = int(input())

road = list(map(int, input().split())) # n-1개
price = list(map(int, input().split())) # n개

total_sum = 0

# 첫 주유
total_sum += price[0] * road[0]

for i in range(1, n-1):
    if price[i] == min(price[:-1]):
        total_sum += price[i] * sum(road[i:])
        break
    total_sum += price[i] * road[i]

print(total_sum)