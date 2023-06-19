# 길이가 같고, 안에 든 알파벳 개수가 동일하면 strfry
alphabet = "abcdefghijklmnopqrstuvwxyz"

def counting_array(array):
    result = [0] * 26
    
    for word in array:
        for i, a in enumerate(list(alphabet)):
            if word == a:
                result[i] += 1
    return result

def is_strfry(a, b):
    if counting_array(list(a)) == counting_array(list(b)):
        return True
    else:
        return False

for _ in range(int(input())):
    str1, str2 = input().split()

    if is_strfry(str1, str2) == True:
        print("Possible")
    else:
        print("Impossible")