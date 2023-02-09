from collections import deque
import sys

input = sys.stdin.readline

def bfs(v):
	q = deque([v])
	chk = [False] * (N+1)
	chk[v] = True
	ans = 1
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

ans = [0 for _ in range(N+1)]
for i in range(1, N+1):
	ans[i] = bfs(i)		

for i in range(1, N+1):
	if ans[i] == max(ans):
		print(i, end=" ")