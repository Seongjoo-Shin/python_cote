from collections import deque

def solution(n, computers):
	answer = 0
	graph = {}
	for start in range(n):
		graph[start] = []
		for end,edge in enumerate(computers[start]):
			if edge == 1 and start!=end :
				graph[start].append(end)
	visited=[]
	not_visited =list(graph.keys())
	print('graph : ', graph)
	print('not_visited : ', not_visited)
	while not_visited :
		visited += bfs(graph , not_visited [0])
		not_visited = list(set(graph.keys()) - set(visited))
		answer+=1
	return answer

def bfs(graph, root):
	visited = []
	q = deque([root])

	while q:
		now = q.popleft()
		if now not in visited:
			visited.append(now)
			q += list(set(graph[now]) - set(visited))
	return visited
	


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) # 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])) # 2