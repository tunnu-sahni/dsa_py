class solution:
    def reverseNumber(self, n):
        revNum = 0

        while n > 0:
            lastDigit = n % 10

            revNum = revNum * 10 + lastDigit

            n = n // 10

        return revNum
    
obj = solution()
num = 1234567891011
print(obj.reverseNumber(num))

class solution:
    def reverseNumber(seslf, n):
        revNum = 0

        while n < 0:
            lastDigit = n % 10

            revNum = revNum * 10 + lastDigit

            n = n // 10

        return revNum
    
obj = solution()
num = 12345
print(obj.reverseNumber(num))