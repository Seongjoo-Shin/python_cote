import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(start_x, start_y):
	q = deque()
	q.append((start_x, start_y))
	adj[start_x][start_y] = 0

	while q:
		x, y = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if nx < 0 or nx >= M or ny < 0 or ny >= N:
				continue
			
			if adj[nx][ny] == 1:
				q.append((nx, ny))
				adj[nx][ny] = 0

ans = []
for _ in range(T):
	M, N, K = map(int, input().split())
	adj = [[0] * (N) for _ in range(M)]
	cnt = 0
	for _ in range(K):
		x, y = map(int, input().split())
		adj[x][y] = 1

	for i in range(M):
		for j in range(N):
			if adj[i][j] == 1:
				bfs(i, j)
				cnt += 1

	ans.append(cnt)

for i in ans:
	print(i)