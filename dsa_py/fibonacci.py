#print fibonacci series up to Nth term

# def main():
#     n = 5
#     n = 4
#     n = 3

#     if n == 0:
#         print(0)

#     elif n == 1:
#         print("0 1")

#     else:
#         fib = [0] * (n + 1)
#         fib[0] = 0
#         fib[1] = 1

#         for i in range(2, n + 1):
#             fib[i] = fib[i - 1] + fib[i - 2]

#         print(f"the fibonacci series up to {n}th term:")
#         print(" ".join(str(num) for num in fib))

# if __name__ == "__main__":
#     main()


# def main():
#     s = 4
#     if s == 0:
#         print(0)

#     elif s == 1:
#         print(0)
#     elif s == 2:
#         print("0 2")

#     else:
#         fib = [0] * (s + 1)
#         fib[0] = 0
#         fib[1] = 1

#         for i in range(2, s + 1):
#             fib[i] = fib[i - 2] + fib[i - 2]

#         print(f" the fibonacci series up to {s}th term:")
#         print(" ".join(str(num) for num in fib))

# if __name__ == "__main__":
#     main()


# def main():
#     n = 6

#     if n == 0:
#         print(f"the fibonacci series up to {n}th term:")
#         print(0)

#     else:
#         second_last = 0 
#         last = 1

#         print(f" the fibonacci series up to {n}th term:")
#         print(f"{second_last} {last}", end=" ")

#         for i in range(2, n + 1):
#             cur = last + second_last
#             second_last = last
#             last = cur
#             print(cur, end=" ")

# if __name__ == "__main__":
#     main()


def fibonacci(N):
    if N <= 1:
        return N
    last = fibonacci(N - 1)
    slast = fibonacci(N - 2)

    return last + slast

N = 4
N = 3
N = 0   
print(fibonacci(N))