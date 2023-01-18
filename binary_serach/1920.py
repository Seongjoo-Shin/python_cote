from bisect import bisect_left, bisect_right
N = int(input())
a = sorted(list(map(int, input().split())))
M = int(input())
b = list(map(int, input().split()))

ans = []
for i in b:
	ll = bisect_left(a, i)
	rr = bisect_right(a, i)
	ans.append(1 if rr-ll else 0)

for answer in ans:
	print(answer)