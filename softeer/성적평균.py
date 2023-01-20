N, K = map(int, input().split())

lst = list(map(int, input().split()))

for _ in range(K):
	sum = 0
	a, b = map(int, input().split())
	for i in range(a-1, b):
		sum += lst[i]
	print('{:.2f}'.format(sum / (b-a+1)))
	

