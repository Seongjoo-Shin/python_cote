from collections import deque

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

n = int(input())

m = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def bfs(y, x):
	q = deque()
	q.append((y, x))
	m[y][x] = '0'
	cnt = 0
	while q:
		cnt += 1
		y, x = q.popleft()
		for i in range(4):
			ny = y + dy[i]
			nx = x + dx[i]

			if 0 <= ny < n and 0 <= nx < n and m[ny][nx] == '1':
				m[ny][nx] = '0'
				q.append((ny, nx))		
	return cnt


ans = []
for i in range(n):
	for j in range(n):
		if m[i][j] == '1' :
			ans.append(bfs(i, j))

print(len(ans))
for i in ans:
	print(i)