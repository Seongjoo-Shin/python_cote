lst = list(map(str, input().split("-")))
answer = ""
for i in range(len(lst)):
	answer += lst[i][:1]
print(answer)