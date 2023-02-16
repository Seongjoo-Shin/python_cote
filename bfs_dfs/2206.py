from collections import deque

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

n, m = map(int, input().split())

a = [list(map(int, list(input()))) for _ in range(n)]

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

def bfs(y, x):
	q = deque()
	q.append([y, x, 0])
	visited[y][x][0] = 1
	while q:
		y, x, c = q.popleft()
		if y == n - 1 and x == m - 1:
			return visited[y][x][c]

		for i in range(4):
			ny = y + dy[i]
			nx = x + dx[i]

			if 0 <= ny < n and 0 <= nx < m:
				if a[ny][nx] == 0 and visited[ny][nx][c] == 0:
					q.append([ny, nx, c])
					visited[ny][nx][c] = visited[y][x][c] + 1
				if a[ny][nx] == 1 and c == 0:
					q.append([ny, nx, 1])
					visited[ny][nx][1] = visited[y][x][0] + 1
	return -1

print(bfs(0, 0))
