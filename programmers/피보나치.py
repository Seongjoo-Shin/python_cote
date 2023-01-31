def solution(n):
	lst = [0 for _ in range(n+1)]
	lst[1] = 1
	for i in range(2, n+1):
		lst[i] = lst[i-2] + lst[i-1]
	return lst[n] % 1234567

print(solution(5))