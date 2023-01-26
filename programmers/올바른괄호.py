
def solution(s):
	answer = True
	lst = list(s)
	stk = []
	for ch in lst:
		if ch == '(':
			stk.append(ch)
		else:
			if stk:
				stk.pop()
			else:
				answer = False
				break
	if stk:
		answer = False
	return answer


print(solution("(()("))