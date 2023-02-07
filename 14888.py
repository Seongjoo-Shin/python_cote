N = int(input())
A = list(map(int, input().split()))
a, b, c, d = map(int, input().split())

lst = []

min_value = int(1e9)
max_value = -int(1e9)

def sol(num, idx, add, sub, mul, div):
	global min_value, max_value

	if idx == N:
		max_value = max(max_value, num)
		min_value = min(min_value, num)
		return
	
	if add > 0:
		sol(num + A[idx], idx + 1, add - 1, sub, mul, div)
	if sub > 0:
		sol(num - A[idx], idx + 1, add, sub - 1, mul, div)
	if mul > 0:
		sol(num * A[idx], idx + 1, add, sub, mul - 1, div)
	if div > 0:
		sol(int(num / A[idx]), idx + 1, add, sub, mul, div - 1)

sol(A[0], 1, a, b, c ,d)

print(max_value)
print(min_value)
