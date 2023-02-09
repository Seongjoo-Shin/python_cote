from collections import deque
import sys

input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(start_y, start_x):
	q = deque()
	q.append((start_y, start_x))
	adj[start_y][start_x] = 0
	cnt = 1
	while q:
		y, x = q.popleft()

		for i in range(4):
			ny = y + dy[i]
			nx = x + dx[i]

			if 0 <= ny < n and 0 <= nx < m and adj[ny][nx] == 1:
				adj[ny][nx] = 0
				q.append((ny, nx))
				cnt += 1
	return cnt

n, m = map(int, input().split())

adj = [list(map(int, input().split())) for _ in range(n)]

ans = []
for i in range(n):
	for j in range(m):
		if adj[i][j] == 1:
			ans.append(bfs(i, j))

if len(ans) == 0:
	print(len(ans))
	print(0)
else:
	print(len(ans))
	print(max(ans))
