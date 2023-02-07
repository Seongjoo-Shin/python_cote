N, K = map(int, input().split())

ans = []

for i in range(1, N+1):
	if N % i == 0:
		ans.append(i)
	
if K > len(ans):
	print(-1)
else:
	print(ans[K-1])