import sys
input = sys.stdin.readline

lst = list(map(int, input().split()))
ans = ''
    
if sorted(lst) == lst:
    ans = 'ascending'
elif sorted(lst, reverse=True) == lst:
    ans = 'descending'
else:
    ans = 'mixed'

print(ans)


