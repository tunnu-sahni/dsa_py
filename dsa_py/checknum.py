#check if a number is armstrong number or not

# class ArmstrongChecker:

#     def is_armstrong(num):
#         k = len(str(num))

#         sum = 0
#         n = num

#         while n > 0:
#             id = n % 10

#             sum += id ** k

#             n = n // 10

#         return sum == num
#     number = 153
# if ArmstrongChecker.is_armstrong(number):

#  print(f"{number} is an Armstrong number.")

# else:
#     print(f"{number} is not an Armstrong number.")


class ArmstrongChecker:
    @staticmethod
    def is_armstrong(num):
        temp = num
        power = len(str(num))
        sum = 0

        while temp > 0:
            digit = temp % 10
            sum += digit ** power
            temp //= 10

        return sum == num


# 👇 yaha define kar number
number = int(input("Enter a number: "))

if ArmstrongChecker.is_armstrong(number):
    print("Armstrong number hai")
else:
    print("Armstrong number nahi hai")