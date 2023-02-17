from bisect import bisect_left, bisect_right

N = int(input())
cards = sorted(list(map(int, input().split())))

M = int(input())
qry = list(map(int, input().split()))

ans = []
for q in qry:
	ll = bisect_left(cards, q)
	rr = bisect_right(cards, q)
	ans.append(1 if rr - ll else 0)

print(*ans)
# print(''.join(map(str, ans)))