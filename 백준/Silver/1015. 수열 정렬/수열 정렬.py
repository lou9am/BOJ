n = int(input())
arr = list(map(int, input().split())) # 2 1 3 1
ans = sorted(arr)

p = []
for a in arr:
    p.append(ans.index(a))
    ans[ans.index(a)] = -1

print(*p)