lst = list(input())

right = lst[len(lst) // 2:]
left = lst[:len(lst) // 2]

ll = 0
rr = 0
for i in range(len(lst) // 2):
    ll += int(left[i])
    rr += int(right[i])

if ll == rr:
    print("LUCKY")
else:
    print("READY")