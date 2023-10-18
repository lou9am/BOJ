// 1463
#include <stdio.h>
#include <math.h>

#ifndef max
#define max(a,b)  (((a) > (b)) ? (a) : (b))
#endif

#ifndef min
#define min(a,b)  (((a) < (b)) ? (a) : (b))
#endif

int main(void)
{
    int n = 0;
    const int ARR_SIZE = 1000001;
    int dp[ARR_SIZE];

    scanf("%d", &n);

    for (int i = 2; i <= n; i++) {
        // 현재의 수에서 1을 빼는 경우
        dp[i] = dp[i - 1] + 1;
        
        // 현재의 수가 2로 나누어 떨어지는 경우
        if (i % 2 == 0) {
            dp[i] = min(dp[i], dp[i / 2] + 1);
        }

        // 현재의 수가 3으로 나누어 떨어지는 경우
        if (i % 3 == 0) {
            dp[i] = min(dp[i], dp[i / 3] + 1);
        }

    }
    printf("%d", dp[n]);

    return 0;
}