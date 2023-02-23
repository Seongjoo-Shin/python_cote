from itertools import permutations
import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
ans = 0
for a in permutations(lst, n):
    summ = 0
    for i in range(1, n):
        summ += abs(a[i-1] - a[i])
    ans = max(summ, ans)
print(ans)