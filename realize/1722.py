n = int(input())
tmp = list(map(int, input().split()))

c, nums = tmp[0], tmp[1:]

factorial = [0] * 21
factorial[0] = 1

for i in range(1, 21):
	factorial[i] = factorial[i-1] * i

if c == 1:
	ans = []
	nums = nums[0]
	used = [0] * (n + 1)

	for i in range(n):
		for j in range(1, n+1):
			if used[j] == 1:
				continue
			if factorial[n-i-1] < nums:
				nums -= factorial[n-i-1]
			else:
				used[j] = 1
				ans.append(j)
				break
	print(*ans)
elif c == 2:
	ans = 0
	used = [0] * (n+1)
	for i in range(n):
		for j in range(1, nums[i]):
			if used[j] == 0:
				ans += factorial[n-1-i]
		used[nums[i]] = 1
	print(ans+1)