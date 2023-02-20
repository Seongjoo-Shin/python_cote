import sys

input = sys.stdin.readline
n = int(input())

p = []

for _ in range(n):
	p.append(int(input()))

p.sort()

ans = 0
for i in range(1, n+1):
	ans += abs(i - p[i-1])

print(ans)