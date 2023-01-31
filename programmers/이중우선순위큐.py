def solution(operations):
	answer = []
	q = []
	for oper in operations:
		a, b = map(str, oper.split())
		if a == 'I':
			q.append(int(b))
			q.sort()
		else :
			if q:
				if b == "1":
					temp = max(q)
					q.remove(temp)
				elif b == "-1" :
					temp = min(q)
					q.remove(temp)

	if q:
		answer = [max(q), min(q)]
	else:
		answer = [0, 0]

	return answer
	

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
