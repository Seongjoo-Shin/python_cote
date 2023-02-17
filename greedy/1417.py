n = int(input())
ds = int(input())
chk = []
ans = 0
for _ in range(n-1):
	chk.append(int(input()))

chk.sort(reverse=True)

if n == 1:
	print(0)
else:
	while chk[0] >= ds:
		ds += 1
		chk[0] -= 1
		ans += 1
		chk.sort(reverse=True)
	print(ans)
