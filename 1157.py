from collections import Counter

lst = list(input().lower())

cnter = sorted(Counter(lst).items(), key=lambda x: -x[1])

chk = 1
tmp = cnter[0][1]
for i in range(1, len(cnter)):
	
	if cnter[i][1] == tmp:
		chk += 1

if chk > 1:
	print('?')
else:
	print(cnter[0][0].upper())