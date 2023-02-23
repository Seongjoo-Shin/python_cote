n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))

s = []

def dfs():
	if len(s) == m:
		print(' '.join(map(str, s)))
		return
	
	for i in range(len(lst)):
		if lst[i] not in s:
			s.append(lst[i])
			dfs()
			s.pop()

dfs()
