import math
class solution:
    def getDivisors(self, N):
        res = []

        for i in range(1, int(math.isqrt(N)) + 1):
            if N % i == 0:
                res.append(i)

                if i != N // i:
                    res.append(N // i)

        return res
    
sol = solution()
N = 36
N = 100
N = 350
result = sol.getDivisors(N)
print("Divisors of", N, ":", *result)