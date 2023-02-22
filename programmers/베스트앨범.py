def solution(genres, plays):
	answer = []

	dict = {}
	tmp = []
	for i,g in enumerate(genres):
		tmp.append([i, g, plays[i]])
		
	tmp.sort(key=lambda x: (x[1], x[2]), reverse=True)

	for i in range(len(genres)):
		if dict.get(genres[i]):
			dict[genres[i]] += plays[i]
		else :
			dict[genres[i]] = plays[i]
	
	s_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)

	for i in s_dict:
		cnt = 2
		for gg in tmp:
			if i[0] == gg[1] and cnt != 0:
				answer.append(gg[0])
				cnt -= 1
	
	return answer



print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])) # [4, 1, 3, 0]
print(solution(["classic", "pop", "classic", "classic"], [800, 600, 150, 800])) # [4, 1, 3, 0]