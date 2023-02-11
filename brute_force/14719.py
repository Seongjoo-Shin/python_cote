H, W = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0

tmp = lst[0]
for i in range(1, W-1):
	l_max = max(lst[:i])
	r_max = max(lst[i+1:])
	
	tmp = min(l_max, r_max)

	if lst[i] < tmp:
		ans += (tmp - lst[i])

print(ans)
# 4 4
# 3 0 1 4

# 4 8
# 3 1 2 3 4 1 1 2

# 3 5
# 0 0 0 2 0