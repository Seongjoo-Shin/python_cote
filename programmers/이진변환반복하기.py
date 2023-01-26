def solution(s):
	cnt = 0
	ccnt = 0
	while True:
		if s == '1':
			break
		cnt = cnt + s.count("0")
		s = s.replace("0","")
		s = bin(len(s))[2:]
		ccnt += 1
	return [ccnt, cnt]

print(solution("110010101001"))