# 1182 : 부분수열의 합
n, s = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0

def backtracking(data, sol, level):
    global cnt
    if sol and sum(sol) == s:
        cnt +=1

    for i in range(level, n):
        sol.append(data[i])
        backtracking(data, sol, i+1)
        sol.pop()
        
backtracking(arr, [], 0)  
print(cnt)