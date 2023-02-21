n = int(input())
ans = n

for i in range(n):
	lst = list(input())
	for j in range(0, len(lst)-1):
		if lst[j] == lst[j+1]:
			pass
		elif lst[j] in lst[j+1:]: 
			ans -= 1
			break

print(ans)

