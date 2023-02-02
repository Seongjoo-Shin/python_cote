def solution(arr):
	arr.sort()
	temp = arr[0]
	for i in range(1, len(arr)):
		for j in range(temp, temp * arr[i] + 1):
			if j % temp == 0 and j % arr[i] == 0:
				temp = j
				break
	return temp
print(solution([2, 6, 8, 14])) # 168
# print(solution([1, 2, 3]))     # 6
