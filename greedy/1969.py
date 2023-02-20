import sys
input = sys.stdin.readline
n, m = map(int, input().split())

dna = [input().rstrip() for _ in range(n)]

sum = 0
ans = ''
for i in range(m):
	dd = [0, 0, 0, 0]

	for j in range(n):
		if dna[j][i] == 'A':
			dd[0] += 1
		elif dna[j][i] == 'C':
			dd[1] += 1
		elif dna[j][i] == 'G':
			dd[2] += 1
		elif dna[j][i] == 'T':
			dd[3] += 1
	tmp = dd.index(max(dd))

	if tmp == 0:
		ans += 'A'
	elif tmp == 1:
		ans += 'C'
	elif tmp == 2:
		ans += 'G'
	elif tmp == 3:
		ans += 'T'
	sum += n - max(dd)

print(ans)
print(sum)