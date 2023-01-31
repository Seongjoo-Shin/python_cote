# 조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
# 조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
# 조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.

def solution(n):
	answer = 0
	bc = bin(n)[2:]
	gg = 0
	for i in bc:
		if i == "1":
			gg += 1
		else:
			continue	
	while True:
		n+=1
		bbc = bin(n)[2:]
		chk = 0
		for i in bbc:
			if i == "1":
				chk += 1
			else:
				continue	
		if gg == chk:
			answer = n
			break
	return answer

print(solution(78))