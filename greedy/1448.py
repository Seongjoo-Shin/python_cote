import sys
input = sys.stdin.readline
n = int(input())

tri = []
for _ in range(n):
	tri.append(int(input()))

tri.sort(reverse=True)

ans = 0

for i in range(len(tri)-2):
	if tri[i] < tri[i+1] + tri[i+2]:
		ans = tri[i] + tri[i+1] + tri[i+2]
		break
	else:
		ans = -1

print(ans)