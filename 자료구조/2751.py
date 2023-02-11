import sys
input = sys.stdin.readline

N = int(input())

ans = []

for _ in range(N):
    ans.append(int(input()))

ans.sort()

for i in ans:
    print(i)