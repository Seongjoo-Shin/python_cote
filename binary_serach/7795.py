import bisect
import sys

input = sys.stdin.readline

ans = []
for _ in range(int(input())):
	N, M = map(int, input().split())
	A = sorted(list(map(int, input().split())))
	B = sorted(list(map(int, input().split())))
	cnt = 0
	for a in A:
		cnt += (bisect.bisect(B, a-1))
	ans.append(cnt)

for a in ans:
	print(a)



# 심해에는 두 종류의 생명체 A와 B가 존재한다. A는 B를 먹는다. A는 자기보다 크기가 작은 먹이만 먹을 수 있다. 예를 들어, A의 크기가 {8, 1, 7, 3, 1}이고, B의 크기가 {3, 6, 1}인 경우에 A가 B를 먹을 수 있는 쌍의 개수는 7가지가 있다. 8-3, 8-6, 8-1, 7-3, 7-6, 7-1, 3-1

# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 A의 수 N과 B의 수 M이 주어진다. 둘째 줄에는 A의 크기가 모두 주어지며, 셋째 줄에는 B의 크기가 모두 주어진다. 크기는 양의 정수이다. (1 ≤ N, M ≤ 20,000) 


# 2
# 5 3
# 8 1 7 3 1
# 3 6 1
# 3 4
# 2 13 7
# 103 11 290 215

# 7
# 1