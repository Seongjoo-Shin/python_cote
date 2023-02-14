n, m = map(int, input().split())
lst = list(map(int, input().split()))

sum = 0
ans = 0

end = 0

for start in range(len(lst)):
	while sum < m and end < n:
		sum += lst[end]
		end += 1
	if sum == m:
		ans += 1
	sum -= lst[start]
	

print(ans)