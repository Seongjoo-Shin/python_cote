N = int(input())

ans = 0
if N < 100:
	ans = N
	print(ans)
else:
	ans = 99
	for i in range(110, N+1):
		a = i // 100
		b = (i - (a*100)) // 10
		c = (i - (a*100) - (b*10))
		if (a + c) / 2 == b:
			ans+=1

print(ans)