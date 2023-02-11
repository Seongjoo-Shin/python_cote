import sys
input = sys.stdin.readline
n = int(input())

def cal(n):
	if n <= 1:
		return n
	else:
		return cal(n-1) + cal(n-2)

print(cal(n))