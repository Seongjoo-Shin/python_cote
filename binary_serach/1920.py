from bisect import bisect_left, bisect_right
N = int(input())
a = sorted(list(map(int, input().split())))
M = int(input())
b = list(map(int, input().split()))

ans = []
for i in b:
	ll = bisect_left(a, i)
	rr = bisect_right(a, i)
	ans.append(1 if rr-ll else 0)

for answer in ans:
	print(answer)


# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오

# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -2^31 보다 크거나 같고 2^31보다 작다.

# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5

# 1
# 1
# 0
# 0
# 1