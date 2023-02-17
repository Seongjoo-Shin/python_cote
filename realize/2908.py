a, b = map(int, input().split())

aa = list(map(int, str(a)))
bb = list(map(int, str(b)))

aaa = ''
bbb = ''
for i in range(2, -1, -1):
	aaa += str(aa[i])
	bbb += str(bb[i])
	
print(aaa if int(aaa) > int(bbb) else bbb)