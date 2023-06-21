# 1475
num = [int(x) for x in input()] # 1~100만
digit = [0] * 10

for n in num:
    digit[n] += 1

tmp = digit[6] + digit[9]
if tmp % 2 == 0:
    digit[6], digit[9] = tmp // 2, tmp // 2
else:
    digit[6], digit[9] = tmp // 2 + 1, tmp // 2 + 1
    
print(max(digit))