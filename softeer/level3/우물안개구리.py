import sys
input = sys.stdin.readline

N, M = map(int, input().split())
weight = list(map(int, input().split()))

ans = [1] * N

for _ in range(M):
  a, b = map(int, input().split())
  if weight[a-1] > weight[b-1]:
    ans[b-1] = 0
  elif weight[a-1] < weight[b-1]:
    ans[a-1] = 0
  else:
    ans[a-1] = 0
    ans[b-1] = 0

cnt = 0
for i in ans:
  if i == 1:
    cnt += 1

print(cnt)
  