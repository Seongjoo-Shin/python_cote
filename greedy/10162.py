time = int(input())

btns = [300, 60, 10]

ans = ""

for btn in btns:
	ans += (str(time // btn) + " ")
	time %= btn

if time > 0:
	print(-1)
else :
	print(ans)
