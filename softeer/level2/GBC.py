import sys
input = sys.stdin.readline
N, M = map(int, input().split())

limit = []
diff = []
chk = 0
for _ in range(N):
	a, b = map(int, input().split())
	tmp = [0] * a
	for i in range(a):
		tmp[i] = b
	limit += tmp

for _ in range(M):
	a, b = map(int, input().split())
	tmp = [0] * a
	for i in range(a):
		tmp[i] = b
	diff += tmp

ans = [0] * 100
for i in range(100):
	ans[i] = (diff[i] - limit[i])
	if ans[i] < 0:
		ans[i] = 0
print(max(ans))