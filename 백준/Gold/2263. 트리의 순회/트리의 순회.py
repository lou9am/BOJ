# 트리 : 트리의 순회 (중위, 후위 순회 주어졌을 때 전위 순회 구하기)
import sys
sys.setrecursionlimit(10**6)

ans = []
def daq(in_start,in_end,post_start,post_end):
    if (in_start > in_end) or (post_start > post_end):
        return
    root = post_order[post_end]
    size = pos[root] - in_start
    ans.append(root)
    
    daq(in_start, pos[root]-1, post_start, post_start + size - 1)
    daq(pos[root]+1, in_end, post_start + size, post_end - 1)

n = int(input())
in_order = [-1]+list(map(int,input().split()))
post_order = [-1]+list(map(int,input().split()))

# pos = [i for i in range(n+1)]
pos = [-1] * (n+1)
for i in range(n+1):
    pos[in_order[i]] = i

daq(1,n,1,n)
print(*ans)