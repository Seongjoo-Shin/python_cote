MOD = 1_000_000_007
K, P, N = map(int, input().split())
	
print((K * (P ** N)) % MOD)
