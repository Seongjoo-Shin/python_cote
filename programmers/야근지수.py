def solution(n, works):
	if sum(works) <= n:
		return 0
	works.sort(reverse=True)
	cnt=n
	while cnt:
		for i in range(len(works)):
			if cnt==0 or works[0]>works[i]:
				break
			works[i]-=1
			cnt-=1

	return sum([w*w for w in works])

print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(3, [1, 1]))