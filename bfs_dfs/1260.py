from collections import deque

N, M, V = map(int, input().split())

adj = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
	a, b = map(int, input().split())
	adj[a][b] = adj[b][a] = 1

chkd = [False] * (N+1)
chkb = [False] * (N+1)

def dfs(now):
	chkd[now] = True
	print(now, end = " ")
	for nxt in range(1, N+1):
		if adj[now][nxt] == 1 and chkd[nxt] == False:
			chkd[nxt] = True
			dfs(nxt)

def bfs(now):
	chkb[now] = True
	q = deque()
	q.append(now)

	while q:
		rn = q.popleft()
		print(rn, end=" ")
		for nxt in range(1, N+1):
			if adj[rn][nxt] == 1 and chkb[nxt] == False:
				chkb[nxt] = True
				q.append(nxt)				

dfs(V)
print()
bfs(V)
