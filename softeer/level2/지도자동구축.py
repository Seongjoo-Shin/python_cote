import sys
input = sys.stdin.readline

N = int(input())

lst = [0] * 16

lst[0] = 2
lst[1] = 3


if N == 1:
	print(pow(lst[N], 2))
elif N > 1:
	for i in range(2, N+1):
		lst[i] = lst[i-1] + lst[i-1] - 1
	print(pow(lst[N], 2))