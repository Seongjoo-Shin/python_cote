import heapq

n = int(input())

ans = 0
con = []
for _ in range(n):
	con.append(list(map(int, input().split())))

con.sort(key=lambda x: (x[0], x[1]))
h = []

for s, e in con:
	if h and h[0] <= s:
		heapq.heappop(h)
	heapq.heappush(h, e)

print(len(h))