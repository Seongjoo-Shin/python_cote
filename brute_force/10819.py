n = int(input())
lst = list(map(int, input().split()))

lst.sort()

ans = 0

if n % 2 == 0:
    s = lst[:n//2]
    b = lst[n//2:]
    aa = []
    for i in range(n//2-1, -1, -1):
        aa.append(s[i])
        aa.append(b[i])
    for i in range(1, n):
        ans += abs(aa[i-1] - aa[i])
else : 
    s = lst[:n//2+1]
    b = lst[n//2+1:]
    aa = []
    for i in range(n//2, -1, -1):
        print(i)
        aa.append(s[i])
        if i != 0:
            aa.append(b[i-1])
    for i in range(1, n):
        ans += abs(aa[i-1] - aa[i])


print(ans)
# 8 20 4 15 1 
# 
# 