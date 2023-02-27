a, b, c = map(int, input().split())

result = 0

if a == b and b == c and c == a:
    result = 10000 + a * 1000
elif a == b or a == c:
    result = 1000 + a * 100
elif b == c:
    result = 100 + b * 100
else:
    result = max(a, max(b, c)) * 100

print(result)