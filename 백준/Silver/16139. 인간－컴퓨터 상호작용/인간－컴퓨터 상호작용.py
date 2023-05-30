# 인간-컴퓨터 상호작용
s = str(input())
q = int(input())

for _ in range(q):
    a, l, r = input().split()
    l, r = int(l), int(r)
 
    cnt = 0
    cnt = s[l:r+1].count(a)

    print(cnt)