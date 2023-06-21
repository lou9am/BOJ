# 1919
alphabet = "abcdefghijklmnopqrstuvwxyz"

def counting(array):
    result = [0] * 26
    for a in array:
        for idx, al in enumerate(alphabet):
            if a == al:
                result[idx] += 1
    return result

first = counting(input())
second = counting(input())

result = 0
for f, s in zip(first, second):
    result += abs(f-s)
print(result)