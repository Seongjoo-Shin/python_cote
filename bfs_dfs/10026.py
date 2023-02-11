from collections import deque

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(x, y, col):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < N and 0 <= nx < N and not visited[nx][ny] and section[nx][ny] == col:
                visited[nx][ny] = True
                q.append((nx, ny))

N = int(input())
section = [list(input()) for _ in range(N)]

cnt1 = 0
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, section[i][j])
            cnt1 += 1


for i in range(N):
    for j in range(N):
        if section[i][j] == 'G':
            section[i][j] = 'R'

cnt2 = 0
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, section[i][j])
            cnt2 += 1



print(cnt1, cnt2)

