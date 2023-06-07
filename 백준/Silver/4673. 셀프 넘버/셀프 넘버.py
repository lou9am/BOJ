MAX = 10000

def self_number(num):
    lst = [int(x) for x in str(num)]
    dn = sum(lst) + num
    return dn

numbers = [i for i in range(1, MAX+1)]
tmp = []

for i in range(1, MAX+1):
    tmp.append(self_number(i))

for i in range(1, MAX+1):
    if i not in tmp:
        print(i)