n, m = map(int, input().split())
sharks = []

for i in range(n):
    tmp = list(map(int, input().split()))
    for j, t in enumerate(tmp):
        if t == 1:
            sharks.append((i, j))

res = -1

for i in range(n):
    for j in range(m):
        md = 1e9
        for x, y in sharks:
            dist = max(abs(i - x), abs(j - y))
            md = min(md, dist)
        
        res = max(md, res)

print(res)