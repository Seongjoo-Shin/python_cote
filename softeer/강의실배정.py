import sys
import heapq

input = sys.stdin.readline

N = int(input())

q = []

for _ in range(N):
  a, b = map(int, input().split())
  heapq.heappush(q, (b, a))

start = 0
ans = 0
while q:
  b, a = heapq.heappop(q)
  if a >= start:
    ans += 1
    start = b

print(ans)
