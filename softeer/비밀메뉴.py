import sys
input = sys.stdin.readline

M, N, K = map(int, input().split())
key = input().strip()
btn = input().strip()

if key in btn:
	print('secret')
else:
	print('normal')