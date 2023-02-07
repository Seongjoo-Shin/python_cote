ans = []
temp = 0
for _ in range(10):
	a, b = map(int, input().split())
	temp -= a
	temp += b
	ans.append(temp)

print(max(ans))