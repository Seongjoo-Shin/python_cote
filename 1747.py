n = int(input())

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def find_next_prime(n):
    num = n
    while True:
        if is_prime(num):
            return num
        num += 1

def is_palindrome(n):
    str_n = str(n)
    return str_n == str_n[::-1]

def find_palindrome(n):
    while True:
        if is_palindrome(n):
            return n
        n += 1

while True:
	if is_palindrome(n) and is_prime(n):
		print(n)
		break
	else:
		n += 1
