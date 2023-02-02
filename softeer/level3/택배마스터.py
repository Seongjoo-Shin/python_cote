from itertools import permutations
import sys
input = sys.stdin.readline

def solution(r, k, m):
	cnt, temp, bag = -1, 0, 0
	for _ in range(k):
		while temp <= m:
			cnt = (cnt + 1) % N
			temp += r[cnt]
		temp -= r[cnt]
		cnt -= 1
		bag += temp
		temp = 0
	
	return bag

N, M, K = map(int, input().split())
lst = list(map(int, input().split()))

rails = list(permutations(lst))

ans = []

for r in rails:
	ans.append(solution(r, K, M))

print(min(ans))