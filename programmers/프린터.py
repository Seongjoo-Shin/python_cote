from collections import deque

def solution(priorities, location):
	answer = 0

	q = deque([(v, i) for i, v in enumerate(priorities)])
	
	while len(q):
		item = q.popleft()
		print(item)
		if q and max(q)[0] > item[0]:
			q.append(item)
		else:
			answer += 1
			if item[1] == location:
				break
	return answer

print(solution([2, 1, 3, 2], 2))    # 1
print(solution([1, 1, 9, 1, 1, 1], 0)) # 5