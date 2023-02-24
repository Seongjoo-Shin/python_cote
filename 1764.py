import sys

input = sys.stdin.readline

n, m = map(int, input().split())

d = set(input().rstrip() for _ in range(n))
b = set(input().rstrip() for _ in range(m))

ans = sorted(list(d & b))

print(len(ans))
for i in ans:
    print(i)