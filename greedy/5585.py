N = 1000 - int(input())

change = [500, 100, 50, 10, 5, 1]

cnt = 0
for i in change:
	cnt += N // i
	N %= i

print(cnt)