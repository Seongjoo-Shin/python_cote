n = list(map(int, input()))

ans = [0] * 10

for i in n:
	if i == 9 or i == 6:
		if ans[6] <= ans[9]:
			ans[6] += 1
		else:
			ans[9] += 1
	else:
		ans[i] += 1

print(max(ans))



