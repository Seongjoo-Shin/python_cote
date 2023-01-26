def solution(A, B):
	len_lst = len(A)
	sum = 0
	A.sort()
	B.sort(reverse=True)
	for i in range(len_lst):
		sum += A[i] * B[i]

	return sum


print(solution([1,2], [3,4]))