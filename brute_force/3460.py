T = int(input())
ans = []
for _ in range(T):
	num = int(input())
	lst = list(bin(num)[2:][::-1])
	for i in range(len(lst)):
		if lst[i] == '1':
			ans.append(i)
			print(i, end=" ")

	ans = []