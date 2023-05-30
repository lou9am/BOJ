# 트리 : 이진 검색 트리 (전위 순회 주어졌을 때 후위 순회 구하기)
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

pre_ordered = []
while True:
    try:
        pre_ordered.append(int(input())) # 루트 - 왼 - 오
    except:
        break

def postorder(s, e):
    if s > e:
        return
    mid = e + 1                         # 오른쪽 노드가 없을 경우

    for i in range(s+1, e+1):
        if pre_ordered[s] < pre_ordered[i]:
            mid = i
            break

    postorder(s+1, mid-1)               # 왼쪽 확인
    postorder(mid, e)                   # 오른쪽 확인
    print(pre_ordered[s])

# __main__
postorder(0, len(pre_ordered)-1) # 시작 인덱스, 끝 인덱스