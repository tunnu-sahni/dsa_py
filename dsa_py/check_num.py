#check if a number is prime or not

class solution:
    def checkPrime(n):
        cnt = 0

        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                cnt += 1

                if n // i != i:
                    cnt += 1

        return cnt ==2
    n = 1482
    isPrime = checkPrime(n)

    number = int(input("enter the number :"))

    if isPrime:
        print(f"{n} is a prime number.")

    else:
        print(f"{n} is not a prime number.")