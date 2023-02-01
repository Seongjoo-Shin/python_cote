# n개의 곱이 가장 큰 경우는 공평하게 나눈 값을 곱하거나 나머지를 더해서 곱하는 경우가 가장 크다는 아이디어에서 해결
def solution(n, s):
	answer = []
	if n > s:
		return [-1]
	p, q = divmod(s, n)
	answer = [p] * n

	for i in range(q):
		answer[i] += 1
	return sorted(answer)


print(solution(2, 9))
print(solution(2, 1))
print(solution(3, 8))