n = int(input()) # 1 <= n <= 10^6
dp = [0 for _ in range(10 ** 6 + 1)]

# 수식이 필요 없는 초기값
dp[1] = 0

for i in range(2, n + 1):
    # 현재의 수에서 1을 빼는 경우
    dp[i] = dp[i - 1] + 1

    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])