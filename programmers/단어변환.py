# 1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
# 2. words에 있는 단어로만 변환할 수 있습니다.
from collections import deque

def solution(begin, target, words):
	answer = 0

	q = deque()
	q.append([begin, 0])

	visited = [0] * len(words)
	while q:
		word, cnt = q.popleft()
		if word == target:
			answer = cnt
			break
		
		for i in range(len(words)):
			temp = 0 
			if not visited[i]:
				for j in range(len(word)):
					if word[j] != words[i][j]:
						temp += 1
				if temp == 1:
					q.append([words[i], cnt+1])
					visited[i] = 1

	return answer

		
	

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])) # 4
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))        # 0