def solution(brown, yellow):
	answer = []
	total = brown + yellow

	for b in range(1, total+1):
		if (total % b) / 1 == 0:
			a = total // b
			if a >= b:
				if 2*a + 2*b == brown + 4:
					return [a, b]
			
	return answer


print(solution(10, 2))   # [4, 3]
print(solution(8, 1))    # [3, 3]
print(solution(24, 24))  # [8, 6]
# 2a + 2b = brown
# (a-2)(b-2) = yellow
# a * b = brown + yellow