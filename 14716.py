from collections import deque

dy = (0, 1, 0, -1, 1, 1, -1, -1)
dx = (1, 0, -1, 0, 1, -1, 1, -1)

def bfs(start_y, start_x):
	q = deque()
	q.append((start_y, start_x))
	adj[start_y][start_x] = 0
	while q:
		y, x = q.popleft()
		
		for i in range(8):
			ny = y + dy[i]
			nx = x + dx[i]

			if (0 <= ny < N) and (0 <= nx < M) and  adj[ny][nx] == 1:
				adj[ny][nx] = 0
				q.append((ny, nx))

N, M = map(int, input().split())
adj = [list(map(int, input().split())) for _ in range(N)]
chk = [[False] * M for _ in range(N)]

cnt = 0
for i in range(N):
	for j in range(M):
		if adj[i][j] == 1:
			bfs(i, j)
			cnt+=1
print(cnt)