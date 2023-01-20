MOD = 1_000_000_007
K, P, N = map(int, input().split())

print(K*pow(P, N*10, MOD) % MOD)