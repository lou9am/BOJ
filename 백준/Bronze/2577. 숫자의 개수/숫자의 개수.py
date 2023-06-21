a = int(input())
b = int(input())
c = int(input())
multiply = [int(x) for x in str(a * b * c)]

result = [0] * 10
for m in multiply:
    result[m] += 1

print(*result, sep = '\n')