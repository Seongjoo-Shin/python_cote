N = input()

ans = 0

N = sorted(N, reverse=True)

if '0' not in N:
	print(-1)
else:
	for i in N:
		ans += int(i)
	
	if ans % 3 != 0:
		print(-1)
	else :
		print(''.join(N))
