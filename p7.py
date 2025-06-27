MOD = 10**9 + 7

def modinv(x):
    return pow(x, MOD - 2, MOD)

class Solution:
    def countGoodArrays(self, n, m, k):
        fact = [1] * n
        inv_fact = [1] * n

        for i in range(1, n):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact[n - 1] = modinv(fact[n - 1])
        for i in range(n - 2, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD

        c = comb(n - 1, k)
        power = pow(m - 1, n - k - 1, MOD) if n - k - 1 >= 0 else 1
        result = c * m % MOD
        result = result * power % MOD
        return result


n = 5
m = 3
k = 2

sol = Solution()
output = sol.countGoodArrays(n, m, k)
print("Result:", output)
