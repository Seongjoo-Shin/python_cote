from collections import deque
import sys

input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

n = int(input())

m = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def bfs(y, x):
	q = deque()
	q.append((y, x))
	visited[y][x] == True
	cnt = 0
	while q:
		y, x = q.popleft()

		for i in range(4):
			ny = y + dy[i]
			nx = x + dx[i]

			if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and m[ny][nx] == '1':
				visited[ny][nx] = True
				q.append((ny, nx))
				cnt += 1
	return cnt

ans = []
for i in range(n):
	for j in range(n):
		if m[i][j] == '1' and not visited[i][j]:
			ans.append(bfs(i, j))

print(len(ans))
for i in ans:
	print(i)

print()

for r in visited:
	print(r)
	