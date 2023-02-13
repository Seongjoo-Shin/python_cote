from itertools import combinations
from copy import deepcopy

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]

poss = [(nn, mm) for nn in range(n) for mm in range(m) if a[nn][mm] == 0]

answer = 0

for tt in combinations(poss, 3):
	tmp_a = deepcopy(a)

	for xx, yy in tt:
		tmp_a[xx][yy] = 1

	virus = [(nn, mm) for nn in range(n) for mm in range(m) if tmp_a[nn][mm] == 2]
	while virus:
		x, y = virus.pop()
		for i in range(4):
			ny = y + dy[i]
			nx = x + dx[i]

			if 0 <= nx < n and 0 <= ny < m and tmp_a[nx][ny] == 0:
				tmp_a[nx][ny] = 2
				virus.append((nx, ny))

	cnt = 0	
	for rr in tmp_a:
		cnt += rr.count(0)
	answer = max(cnt, answer)

print(answer)