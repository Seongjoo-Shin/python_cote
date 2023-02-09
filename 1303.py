from collections import deque
N, M = map(int, input().split())

a = [list(input()) for _ in range(M)]
visited = [[False] * N for _ in range(M)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def is_valid_coord(x, y):
	return 0 <= y < N and 0 <= x < M

def bfs(x, y, color):
	q = deque()
	q.append((x, y))
	visited[x][y] = True
	cnt = 0
	while q:
		x, y = q.popleft()

		for i in range(4):
			ny = y + dy[i]
			nx = x + dx[i]

			if is_valid_coord(nx, ny) and not visited[nx][ny] and a[nx][ny] == color:
				visited[nx][ny] = True
				q.append((nx, ny))
				cnt += 1
	return cnt + 1

white, blue = 0, 0
for i in range(M):
	for j in range(N):
		if a[i][j] == 'W' and not visited[i][j]:
			white += bfs(i, j, 'W') ** 2
		elif a[i][j] =='B' and not visited[i][j]:
			blue += bfs(i, j, 'B') ** 2

print(white, blue)

