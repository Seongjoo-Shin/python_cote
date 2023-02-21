n = int(input())

lst = []
ans = []
for _ in range(n):
	lst.append(list(map(int, input().split())))

for i in range(len(lst)):
	r = 1
	for j in range(n):
		if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
			r += 1
	print(r, end=' ')