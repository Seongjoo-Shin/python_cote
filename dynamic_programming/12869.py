import sys
from itertools import permutations

input = sys.stdin.readline

def answer(x, y, z, cnt):
	global ans
	if x <= 0 and y <= 0 and z <= 0:
		if ans > cnt:
			ans = cnt
			return
	
	x = 0 if x <= 0 else x
	y = 0 if y <= 0 else y
	z = 0 if z <= 0 else z

	if dp[x][y][z] <= cnt and dp[x][y][z] != 0:
		return 

	dp[x][y][z] = cnt
	
	for i in permutations([9, 3, 1], 3):
		answer(x - i[0], y - i[1], z - i[2], cnt + 1)

N = int(input())
scv = list(map(int, input().split()))

while len(scv) < 3:
	scv += [0]

ans = 100

dp = [[[100] * (max(scv) + 1) for i in range((max(scv) + 1))] for j in range((max(scv) + 1))]
answer(scv[0], scv[1], scv[2], 0)
# print(dp)
print(ans)