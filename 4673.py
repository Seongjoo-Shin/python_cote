def d(n):
	n = n + sum(map(int, str(n)))
	return n

lst = set()
for i in range(1, 10001):
	lst.add(d(i))

for i in range(1, 10001):
	if i not in lst:
		print(i)