import sys

input = sys.stdin.readline

N = int(input())

ans = []

for _ in range(N):
	a, b = map(int, input().split())
	ans.append([a, b])

ans.sort()

for i in range(N):
	print(ans[i][0], ans[i][1])