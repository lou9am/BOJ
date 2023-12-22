level = []
for _ in range(int(input())):
    level.append(int(input()))

max = level[-1]
cnt = 0

for idx, i in enumerate(reversed(level)):
    if idx == 0:
        continue

    if i >= max:
        cnt += (i - max + 1)
        max -= 1
    else:
        max = i

print(cnt)