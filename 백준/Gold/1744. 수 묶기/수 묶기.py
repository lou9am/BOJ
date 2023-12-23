# 1744
n = int(input())
plus_array, minus_array = [], []

num_zero, result = 0, 0
for _ in range(n):
    num = int(input())
    
    if num > 1:
        plus_array.append(num)
    elif num <= 0:
        minus_array.append(num)
    else:
        result += num

plus_array.sort(reverse = True)
minus_array.sort()

for i in range(0, len(plus_array), 2):
    if i + 1 >= len(plus_array):
        result += plus_array[i]
    else:
        result += (plus_array[i] * plus_array[i + 1])

for i in range(0, len(minus_array), 2):
    if i + 1 >= len(minus_array):
        result += minus_array[i]
    else:
        result += (minus_array[i] * minus_array[i + 1])

print(result)