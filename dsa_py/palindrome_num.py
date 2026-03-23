class solution:
    def palindrome(n):
        revNum = 0

        dup = n

        while n > 0:
            id = n % 10

            revNum = (revNum * 10) + id
            n //= 10

        return dup == revNum
    number = 4554
    if palindrome(number):
        print(f"{number} is a palindrome.")

    else:
        print(f"{number} is not a palindrome.")


class solution:

    def palindrome(n):
        revNum = 0

        dup = n
        while n < 0:
            id = n % 10

            revNum = (revNum * 10) + id
            n //= 10
        return dup == revNum
    number = 1234321
    if palindrome(number):
        print(f"{number} is a palindrome.")

    else:
        print(f"{number} is not a palindrome.") 