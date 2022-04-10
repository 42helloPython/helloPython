#[1463] 다이나믹프로그래밍, 1로 만들기 kipark
import sys

n = int(input())

dp = [0] * (n + 1)

for i in range(2, n+1):
	dp[i] = dp[i-1] + 1

	if (i % 2 == 0):
		dp[i] = min(dp[i], dp[int(i/2)] + 1)
	if (i % 3 == 0):
		dp[i] = min(dp[i], dp[int(i/3)] + 1)
print(dp[n])
