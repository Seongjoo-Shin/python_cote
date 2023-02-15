croa = ['c=', 'c-', 'dz=', 'lj', 'nj', 's=', 'z=']

word = input()

for c in croa:
	word = word.replace(c, '.')
print(len(word))