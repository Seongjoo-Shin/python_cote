N = int(input())
scv = list(map(int, input().split()))
mutal = [9, 3, 1]

answer = 0
while sum(scv) > 0:
	scv.sort(reverse=True)
	for i in range(len(scv)):
		if scv[i] != 0:
			scv[i] -= mutal[i]
	if scv[-1] <= 0:
		scv.pop()
	answer += 1

print(answer)