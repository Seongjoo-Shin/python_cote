brackets = list(input())
stk = []
answer = 0
ans = 1

for i in range(len(brackets)):
	if brackets[i] == '(':
		stk.append(brackets[i])
		ans *= 2
	elif brackets[i] == '[':
		stk.append(brackets[i])
		ans *= 3
	elif brackets[i] == ')':
		if not stk or stk[-1] == '[':
			answer = 0
			break
		if brackets[i-1] == '(':
			answer += ans
		stk.pop()
		ans //= 2
	elif brackets[i] == ']':
		if not stk or stk[-1] == '(':
			answer = 0
			break
		if brackets[i-1] == '[':
			answer += ans
		stk.pop()
		ans //= 3

if stk:
	print(0)
else:
	print(answer)
# (()[[]])([])