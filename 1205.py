n, s, p = map(int, input().split())

if n == 0:
    print(1)
else :
    lst = list(map(int, input().split()))
    if n == p and lst[-1] >= s:
        print(-1)
    else:
        ans = n + 1
        for i in range(n):
            if lst[i] <= s:
                ans = i + 1
                break
        print(ans)