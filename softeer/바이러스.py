MOD = 1_000_000_007
K, P, N = map(int, input().split())

for i in range(N):
	K = (K * P) % MOD
print(K)