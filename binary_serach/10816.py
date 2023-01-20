from bisect import bisect_left, bisect_right

N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
qry = list(map(int, input().split()))
print(cards)
ans = []
for q in qry:
	ll = bisect_left(cards, q)
	rr = bisect_right(cards, q)
	ans.append(rr-ll)

print(*ans)


# 3 0 0 1 2 0 0 2