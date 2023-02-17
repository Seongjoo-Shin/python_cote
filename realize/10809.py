word = input()

alpabet = list(range(97, 123))

for al in alpabet:
	print(word.find(chr(al)))