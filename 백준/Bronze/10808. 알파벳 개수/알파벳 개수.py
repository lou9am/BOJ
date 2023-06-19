s = list(input())
alphabet = "abcdefghijklmnopqrstuvwxyz"
result = [0] * 26

for idx, word in enumerate(s):
    for i, a in enumerate(list(alphabet)):
        if word == a:
            result[i] += 1

print(' '.join(map(str,result)))