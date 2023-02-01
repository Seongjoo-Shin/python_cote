# 자연수 n 개로 이루어진 중복 집합(multi set, 편의상 이후에는 "집합"으로 통칭) 중에 

# 다음 두 조건을 만족하는 집합을 최고의 집합이라고 합니다.

# 각 원소의 합이 S가 되는 수의 집합
# 위 조건을 만족하면서 각 원소의 곱 이 최대가 되는 집합
# 예를 들어서 자연수 2개로 이루어진 집합 중 합이 9가 되는 집합은 다음과 같이 4개가 있습니다.
# { 1, 8 }, { 2, 7 }, { 3, 6 }, { 4, 5 }
# 그중 각 원소의 곱이 최대인 { 4, 5 }가 최고의 집합입니다.

# 집합의 원소의 개수 n과 모든 원소들의 합 s가 매개변수로 주어질 때, 최고의 집합을 return 하는 solution 함수를 완성해주세요.
from itertools import combinations, permutations

def solution(n, s):
	answer = []
	lst = [i for i in range(1, s+1)]
	temp = 1
	lst_set = list(combinations(lst, 2))
	for a, b in lst_set:
		if a+b == s:
			chk = a * b
			if temp < chk:
				temp = chk
				answer = [a, b]
	if s % 2 == 0:
		if temp < pow((s // 2), 2):
			answer = [s//2, s//2]
	
	if not answer:
		answer = [-1]
	return answer


print(solution(2, 9))
print(solution(2, 1))
print(solution(2, 8))