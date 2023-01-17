N = int(input())

ans = 0
if N < 100:
	ans = N
else:
	ans = 99
	for i in range(100, N+1):
		a = i // 100
		b = (i - (a*100)) // 10
		c = (i - (a*100) - (b*10))
		if (a-b) == (b-c):
			ans+=1

print(ans)