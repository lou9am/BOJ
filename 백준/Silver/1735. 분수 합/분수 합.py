# 1735 분수의 합
import math
a, b = map(int, input().split()) # a/b
c, d = map(int, input().split()) # c/d

# 두 분 수의 합을 기약분수로 출력
mother = math.lcm(b, d)
son = (mother // b) * a + (mother // d) * c

# 기약분수로 약분
common = math.gcd(mother, son)
print(son // common, mother // common)