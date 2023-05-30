n = int(input())

array = []
for _ in range(n):
    start, end = map(int, input().split())
    array.append([start, end])

array.sort(key = lambda x: x[0])
array.sort(key = lambda x: x[1]) # 여기 좀 이해가 안 감. end를 기준으로 오름차순 정렬할 거면 윗줄은 없어도 되는데???

cnt = 1
end = array[0][1] # 가장 작은 end값
for i in range(1, n):
    if array[i][0] >= end: # 다음 회의 시간이 안 겹치면
        cnt += 1
        end = array[i][1]

print(cnt)