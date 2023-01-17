from collections import deque
import sys

input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def is_valid_coord(y, x):
	return 0 <= y < n and 0 <= x < m
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

			if is_valid_coord(ny, nx) and adj[ny][nx] == 1:
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

print(len(ans))
print(max(ans))
