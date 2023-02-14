from collections import deque

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

n, m = map(int, input().split())

t = [list(input().strip()) for _ in range(n)]

def bfs(y, x):
	dist = [[0] * m for _ in range(n)]
	q = deque()
	q.append((y, x))
	dist[y][x] = 1
	m_dist = -1
	while q:
		y, x = q.popleft()
		for i in range(4):
			ny = y + dy[i]
			nx = x + dx[i]
			if 0 <= ny < n and 0 <= nx < m and t[ny][nx] == 'L' and dist[ny][nx] == 0:
				q.append((ny, nx))
				dist[ny][nx] = dist[y][x] + 1
				m_dist = max(m_dist, dist[ny][nx])
	return m_dist - 1
ans = 0
for i in range(n):
	for j in range(m):
		if t[i][j] == 'L':
			ans = max(ans, bfs(i, j))

print(ans)
