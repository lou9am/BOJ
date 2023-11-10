n = int(input())

A = list(map(int, input().split()))
A.sort()

B = list(map(int, input().split()))
B.sort(reverse=True)

ans = 0
for a in A:
    ans += a * B.pop(0)

print(ans)