t = int(input())

for _ in range(t):
	n, c = input().split()
	tmp = list(c)

	for i in range(len(tmp)):
		for _ in range(int(n)):
			print(tmp[i], end='')
	print()