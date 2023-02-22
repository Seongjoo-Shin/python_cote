n, k = map(int, input().split())

cc = [list(map(int, input().split())) for _ in range(n)]

cc.sort(key=lambda x: (x[1], x[2], x[3], x[0]), reverse=True)


for i in range(n):
	if cc[i][0] == k:
		index = i

for i in range(n):
	if cc[index][1:] == cc[i][1:]:
		print(i+1)
		break
