from collections import deque

a, b = map(int, input().split())
ans = 0
q = deque([(a, 1)])

while q:
	i, cnt = q.popleft()

	if i == b:
		ans = cnt
		break

	if i * 2 <= b:
		q.append((i * 2, cnt + 1))
	if int(str(i) + '1') <= b:
		q.append((int(str(i) + '1'), cnt + 1))

if ans < 1:
    print(-1)
else:
    print(ans)