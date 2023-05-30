n, k = map(int, input().split())
temp = list(map(int, input().split()))

sum_value = 0
prefix_sum = [0]
for t in temp:
    sum_value += t
    prefix_sum.append(sum_value)

tmp = []
for i in range(n, k-1, -1):
    tmp.append(prefix_sum[i] - prefix_sum[i-k])
print(max(tmp))