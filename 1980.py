n, m, t = map(int, input().split())

coke = t
sum = 0

for i in range((t // n), -1, -1):
    a = i
    for j in range((t // m), -1, -1):
        b = j
        tmp = (n * a) + (m * b)
        if (t - tmp) < coke and (t - tmp) >= 0:
            sum = a + b
            coke = t - tmp
        
        elif (t - tmp) == coke:
            if a + b > sum:
                sum = a + b
                coke = (t - tmp)
print(sum, coke)