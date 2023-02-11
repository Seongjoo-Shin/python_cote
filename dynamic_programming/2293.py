n, k = map(int, input().split())

dp = [0] * (k +  1)
c = []
dp[0] = 1
for _ in range(n):
	c.append(int(input()))

for i in c:
	for j in range(1, k + 1):
		if j - i >= 0:
			dp[j] += dp[j - i]

print(dp[k])
