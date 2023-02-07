brackets = list(map(str, input()))

stk = []
answer = 0
for i in range(len(brackets)):
	if brackets[i] == '(' or brackets[i] == '[':
		stk.append(brackets[i])
	elif brackets[i] == ')':
		if stk[-1] == '(':
			stk.pop()
			answer += 2
	elif brackets[i] == ']':
		if stk[-1] == '[':
			stk.pop()
			answer += 3

print(stk)
print(answer)
# (()[[]])([])