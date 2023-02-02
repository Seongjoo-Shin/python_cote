from collections import deque
import sys

input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(x, y):
	cnt = 1
	q = deque()
	q.append((x, y))
	visited[x][y] = True
	while q:
		x, y = q.popleft()
		for i in range(4):
			ny = y + dy[i]
			nx = x + dx[i]

			if not visited[nx][ny] and lst[nx][ny] == '1':
				q.append((nx, ny))
				lst[ny][nx] = 0

	return cnt


N = int(input())
lst = [[input().split()] for _ in range(N+1)]
visited = [[False] * i for i in range(N+1)]

ans = []
for i in range(N+1):
	for j in range(N+1):
		if not visited[i][j] and lst[i][j] == '1':
			ans.append(bfs(i, j))
print(ans)
