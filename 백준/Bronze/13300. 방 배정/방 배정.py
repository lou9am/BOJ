# 13300 방 배정
n, k = map(int, input().split())
student = [[0] * 2 for _ in range(6)]

for _ in range(n):
    s, y = map(int, input().split()) # s = 0 :여자, 1:남자
    student[y-1][s] += 1
    
result = 0
for s in student:
    female, male = s
    if female == 0:
        pass
    elif female % k == 0:
        result += female // k
    else:
        result += female // k + 1
    
    if male == 0:
        continue
    elif male % k == 0:
        result += male // k
    else:
        result += male // k + 1
    
print(result)