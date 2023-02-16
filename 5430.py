from collections import deque

t = int(input())
for _ in range(t):
	p = input()
	n = int(input())
	lst = deque(input()[1:-1].split(","))

	if n == 0:
		lst = []
	
	flag = 0

	for c in p:
		if c == 'R':
			flag += 1
		elif c == 'D':
			if len(lst) == 0:
				print('error')
				break
			else:
				if flag % 2 == 0:
					lst.popleft()
				else:
					lst.pop()
	
	else:
		if flag % 2 == 0:
			print('['+ ','.join(lst) + ']')
		else:
			lst.reverse()
			print('['+ ','.join(lst) + ']')