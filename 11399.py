N = int(input())
a = list(map(int, input().split()))
a.sort()

ans = 0
for i in range(1, N+1):
	ans += sum(a[0:i])

print(ans)