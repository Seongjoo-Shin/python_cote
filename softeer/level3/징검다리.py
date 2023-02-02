N = int(input())
bridge = list(map(int, input().split()))

ans = [1] * N

for i in range(1, N):
	for j in range(i):
		if bridge[i] > bridge[j]:
			ans[i] = max(ans[i], ans[j]+1)

print(max(ans))
