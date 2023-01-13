N = int(input())

a = []
ans = []
for _ in range(N):
	a.append(int(input()))
a.sort(reverse=True)

for i  in range(N):
	ans.append(a[i] * (i+1))
print(max(ans))