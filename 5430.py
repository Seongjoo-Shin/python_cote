def R(lst): # 뒤집기
	return lst[::-1]

def D(lst): # 맨앞 제거
	return lst[1:]


t = int(input())
flag = 1
for _ in range(t):
	p = list(input())
	n = int(input())
	lst = input()[1:-1].split(",")

	for c in p:
		if c == 'R':
			flag += 1
		elif c == 'D':
			if len(lst) <= 1:
				print('error')
				break
			else:
				if flag % 2 == 0:
					lst.reverse()
					lst = D(lst)
	if lst:
		if flag % 2 == 0:
			lst.reverse()
			print('['+ ','.join(lst) + ']')
		else:
			print('['+ ','.join(lst) + ']')