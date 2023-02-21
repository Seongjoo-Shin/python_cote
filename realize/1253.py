n = int(input())
lst = list(map(int, input().split()))

lst.sort()

result = 0

for i, num in enumerate(lst):
	tmp = lst[:i] + lst[i+1:]
	ll, rr = 0, len(tmp) - 1
	while ll < rr:
		if tmp[ll] + tmp[rr] > num:
			rr -= 1
		elif tmp[ll] + tmp[rr] < num:
			ll += 1
		else:
			result += 1
			break
print(result)