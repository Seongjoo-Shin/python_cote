from collections import deque

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

def is_valid_coord(y, x):
	return 0 <= y < N and 0 <= x < M

def bfs(start_y, start_x):
	q = deque()
	q.append((start_y, start_x))
	res = 1
	while len(q) > 0:
		y, x = q.popleft()
		for k in range(4):
			ny = y + dy[k]
			nx = x + dx[k]
			if is_valid_coord(ny, nx) and adj[ny][nx] == 1:
				q.append((ny, nx))
				adj[ny][nx] = 0
				res += 1
	return res

N, M, K = map(int, input().split())

adj = [[0] * M for _ in range(N)]
for _ in range(1, K+1):
	y, x = map(int, input().split())
	adj[y-1][x-1] = 1


answer = []
for i in range(N):
	for j in range(M):
		if adj[i][j] == 1:
			adj[i][j] = 0
			answer.append(bfs(i, j))

print(max(answer))