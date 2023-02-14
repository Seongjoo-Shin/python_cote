import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
	n = int(input())
	lst = []
	for _ in range(n):
		s, m =  map(int, input().split())
		lst.append([s, m])
	lst.sort()
	tmp = lst[0][1]
	ans = 1
	for i in range(n):
		if tmp > lst[i][1]:
			ans += 1
			tmp = lst[i][1]
	print(ans)