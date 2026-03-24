#factorial of a number

# class solution:
#     def factorial(X):
#         ans = 1

#         for i in range(1, X + 1):
#             ans *= i

#         return ans
#     X = 5
#     X = 3

#     result = factorial(X)

#     print(f"the factorial of {X} is {result}")



class solution:
    def factorial(n):
        if n == 0:
            return 1
        return n * (n - 1)
    n = 3
    n = 5
    print(factorial(n))