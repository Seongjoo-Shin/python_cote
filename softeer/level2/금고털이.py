import sys

input = sys.stdin.readline

W, N = map(int, input().split())

boseoks = [list(map(int, input().split())) for _ in range(N)]

boseoks.sort(key=lambda x: x[1], reverse=True)

ans = 0
cnt = 0

k = 0
while W:
    ans += boseoks[k][1]
    boseoks[k][0] -= 1
    if boseoks[k][0] == 0:
        k += 1
    W -= 1

print(ans)