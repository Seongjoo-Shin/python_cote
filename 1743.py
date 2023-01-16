from collections import deque

N, M, K = map(int, input().split())

adj = [[0] * (M+1) for _ in range(N+1)]

for _ in range(1, K+1):
	a, b = map(int, input().split())
	adj[a][b] = 1

def bfs(v):
	q = deque()
	chk = [False] * (K+1)
	chk[v] = True
	q.append(v)
	ans = 0
	while q:
		now = q.popleft()
		for nxt in range(1, K):
			if adj[now][nxt] == 1 and not chk[nxt]:
				chk[nxt] = True
				q.append(nxt)
				ans += 1
	return ans

answer = []
for i in range(1, K+1):
	answer.append(bfs(i))

print(answer)