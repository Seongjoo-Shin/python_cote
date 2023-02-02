ans = 0

def cal_time(start, end):
	start = a.split(':')
	end = b.split(':')
	min_s = int(start[0]) * 60 + int(start[1])
	min_e = int(end[0]) * 60 + int(end[1])
	return min_e - min_s

for _ in range(5):
	a, b = input().split()
	
	ans += cal_time(a,b)

print(ans)