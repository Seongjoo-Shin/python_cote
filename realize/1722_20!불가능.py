from itertools import permutations

n = int(input())
lst = list(map(int, input().split()))
tmp = []
for i in range(1, n+1):
	tmp.append(i)

per = list(permutations(tmp, n))

if lst[0] == 1:
	for r in per[lst[1]]:
		print(r, end=' ')
else:
	chk = (lst[1:])
	for i, p in enumerate(per):
		if chk == list(p):
			print(i+1)
			break