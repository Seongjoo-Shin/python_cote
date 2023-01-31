def solution(n, words):
	answer = answer = [0,0]
	for i in range(1, len(words)):
		if words[i][0] != words[i-1][len(words[i-1])-1:]:
			answer = [i%n+1, i//n+1]
			break
		elif words[i] in words[:i]:
			answer = [i%n+1, i//n+1]
			break
	return answer


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]	))

print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))

print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))