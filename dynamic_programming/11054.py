A = int(input())
lst = list(map(int, input().split()))

dp = [1 for i in range(A)]
dp1 = [1 for i in range(A)]

dp2 = [0 for i in range(A)]

for i in range(A):
  for j in range(i):
    if lst[i] > lst[j]:
      dp[i] = max(dp[i], dp[j]+1)

lst.reverse()

for i in range(A):
  for j in range(i):
    if lst[i] > lst[j]:
      dp1[i] = max(dp1[i], dp1[j]+1)
dp1.reverse()
for i in range(A):
  dp2[i] = dp[i] + dp1[i]

print(max(dp2) - 1)
