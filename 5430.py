def R(lst): # 뒤집기
	return lst[::-1]

def D(lst): # 맨앞 제거
	return lst[1:]


t = int(input())

for _ in range(t):
	p = list(input())
	n = int(input())
	lst = input()[1:-1].split(",")

	for c in p:
		if c == 'R':
			lst = R(lst)
		elif c == 'D':
			if len(lst) <= 1:
				print('error')
				break
			else:
				lst = D(lst)
	if lst:
		print('['+ ','.join(lst) + ']')