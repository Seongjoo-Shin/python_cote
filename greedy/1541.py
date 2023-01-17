x = input().split('-')

ans = []

for i in x:
	sum = 0
	tmp = i.split('+')
	for j in tmp:
		sum += int(j)
	ans.append(sum)
	
n = ans[0]

for i in range(1, len(ans)):
	n -= ans[i]

print(n)