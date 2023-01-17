N = int(input())
load = list(map(int, input().split()))
price = list(map(int, input().split()))

ans = 0
tmp = price[0]
for i in range(N-1):
	if price[i] < tmp:
		tmp = price[i]
	ans += tmp * load[i]

print(ans)