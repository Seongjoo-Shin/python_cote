def solution(n, works):
	answer = 0
	lw = len(works)
	if sum(works) <= n:
		return 0
	
	works.sort()

	for _ in range(n):
		works[-1] -= 1
		works.sort()


	for i in range(lw):
		answer += pow(works[i], 2)
	return answer

print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(3, [1, 1]))