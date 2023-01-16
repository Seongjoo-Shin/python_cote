from collections import deque
import sys

input = sys.stdin.readline

def bfs(v):
	q = deque([v])
	ans = 0
	chk = [False] * (N+1)
	
	q.append(v)
	chk[v] = True
	
	while q:
		v = q.popleft()
		for nxt in adj[v]:
			if not chk[nxt]:
				q.append(nxt)
				chk[nxt] = True
				ans += 1
	return ans

N, M = map(int, input().split())

adj = [[] for _ in range(N+1)]

for _ in range(1, M+1):
	a, b = map(int, input().split())
	adj[b].append(a)

ans = []
max_value = -1
for i in range(1, N+1):
	s = bfs(i)
	if s > max_value:
		ans = [i]
		max_value = s
	elif s == max_value:
		ans.append(i)
		max_value = s
		

for i in ans:
	print(i, end=" ")