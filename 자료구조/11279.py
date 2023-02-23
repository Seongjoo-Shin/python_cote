import sys
import heapq

input = sys.stdin.readline

n = int(input())

h = []

for _ in range(n):
	tmp = int(input())
	if tmp > 0:
		heapq.heappush(h, -tmp)
	else:
		if not h:
			print(0)
		else:
			print(-heapq.heappop(h))