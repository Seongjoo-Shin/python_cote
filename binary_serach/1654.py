import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lope = []
for _ in range(K):
	lope.append(int(input()))
start = 1
end = max(lope)

while start <= end:
	mid = (start + end) // 2
	cnt = 0
	for i in lope:
		cnt += i // mid
	
	if cnt >= N:
		start = mid + 1
	else :
		end = mid - 1

print(end)