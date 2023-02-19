t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())

    p = [i for i in range(1, n + 1)]

    for kk in range(k):
        for nn in range(1, n):
            p[nn] += p[nn - 1]
    print(p[-1])