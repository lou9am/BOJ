# 10026 : N과 M(1)
from itertools import permutations

n, m = map(int, input().split())

# 1 <= m <= n <= 8
natural_num = [1, 2, 3, 4, 5, 6, 7, 8]
lst = natural_num[0:n]

result = list(permutations(lst, m))

## 튜플의 리스트 2번 언패킹
for i in range(len(result)):
    # 여길 m개 만큼 unpacking
    for j in range(m):
        print(result[i][j], end = ' ')
    print()