n, m = map(int, input().split())

s = []

def dfs():
	if len(s) == m and sorted(s, reverse=True)[::-1] == s:
		print(' '.join(map(str, s)))
		return
	
	for i in range(1, n+1):
		if i not in s:
			s.append(i)
			dfs()
			s.pop()

dfs()
