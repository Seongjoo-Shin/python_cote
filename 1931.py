N = int(input())

ta = []
for _ in range(N):
	a, b = map(int, input().split())
	ta.append([a,b])

ta.sort(key=lambda x:(x[1], x[0]))

t_s = 0
t_e = 0
ans = 0
for start, end in ta:
	if start >= t_e:
		t_s = start
		t_e = end
		ans += 1

print(ans)