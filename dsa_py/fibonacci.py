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


def main():
    s = 4
    if s == 0:
        print(0)

    elif s == 1:
        print(0)
    elif s == 2:
        print("0 2")

    else:
        fib = [0] * (s + 1)
        fib[0] = 0
        fib[1] = 1

        for i in range(2, s + 1):
            fib[i] = fib[i - 2] + fib[i - 2]

        print(f" the fibonacci series up to {s}th term:")
        print(" ".join(str(num) for num in fib))

if __name__ == "__main__":
    main()