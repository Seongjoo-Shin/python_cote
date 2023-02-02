def solution(people, limit):
	answer = 0
	people.sort()

	start = 0
	end = len(people) - 1
	while start < end:
		if people[start] + people[end] <= limit:
			answer += 1
			start += 1
		end -= 1
	return len(people) - answer

print(solution([70, 50, 80, 50], 100))  # 3
print(solution([70, 80, 50], 100))      # 3