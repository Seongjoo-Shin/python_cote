def solution(people, limit):
	answer = 0
	people.sort()
	while people:
		for i in range(len(people)):
			for j in range(2):
					print(i, j)

	return answer

print(solution([70, 50, 80, 50], 100))  # 3
print(solution([70, 80, 50], 100))      # 3