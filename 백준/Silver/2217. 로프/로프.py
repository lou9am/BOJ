n = int(input())

weight = []
for _ in range(n):
    weight.append(int(input()))

weight.sort(reverse = True)

ans = [weight.pop(0)]
for idx, w in enumerate(weight):
    ans.append(w * (idx + 2))

print(max(ans))