import bisect
import sys

input = sys.stdin.readline

ans = []
for _ in range(int(input())):
	N, M = map(int, input().split())
	A = sorted(list(map(int, input().split())))
	B = sorted(list(map(int, input().split())))
	cnt = 0
	for a in A:
		cnt += (bisect.bisect(B, a-1))
	ans.append(cnt)

for a in ans:
	print(a)