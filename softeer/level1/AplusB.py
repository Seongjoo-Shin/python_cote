import sys
input  = sys.stdin.readline
N = int(input())
ans = []
for _ in range(N):
	a, b = map(int, input().split())
	ans.append(a+b)

for i in range(N):
	print('Case #%d: %d' %(i+1, ans[i]))
