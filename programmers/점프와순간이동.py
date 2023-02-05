def solution(n):
    ans = 0
    
    while n > 0:
        ans += n % 2
        n =  n // 2
        print("n : {} // ans : {}".format(n, ans))
    return ans

print(solution(5))    # 2
print(solution(6))    # 2
print(solution(5000)) # 5