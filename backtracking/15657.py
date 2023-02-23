n, m = map(int, input().split())

lst = sorted(list(map(int, input().split())))


s = []

def dfs(ii):
	if len(s) == m:
		print(' '.join(map(str, s)))
		return
	
	for i in range(ii, n):
		s.append(lst[i])
		dfs(i)
		s.pop()

dfs(0)
