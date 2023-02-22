import sys
import heapq

input = sys.stdin.readline

N = int(input())

arr = []

for _ in range(N):
	a, b = map(int, input().split())
	arr.append((a, b))

q = [0]

for a, b in sorted(arr):
	if q[0] <= a:
		heapq.heappop(q)
	heapq.heappush(q, b)
print(len(q))