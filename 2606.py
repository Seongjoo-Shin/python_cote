from collections import deque

N = int(input())
M = int(input())

adj = [[0] * (N+1) for _ in range(N+1)]

for _ in range(1, M+1):
	a, b = map(int, input().split())
	adj[a][b] = adj[b][a] = 1

chk = [False] * (N+1)

ans = []
def bfs(v):
	q = deque()
	q.append(v)
	chk[v] = True

	while q:
		now = q.popleft()
		for nxt in range(1, N+1):
			if adj[now][nxt] == 1 and chk[nxt] == False:
				chk[nxt] = True
				q.append(nxt)
				ans.append(nxt)


bfs(1)

print(len(ans))