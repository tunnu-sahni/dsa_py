#recursive implementation of atoi

# INT_MIN = -2**31
# INT_MAX = 2**31 - 1

# def helpers(s, i, num, sign):
#     if i >= len(s) or not s[i].isdigit():
#         return sign * num
    
#     num = num * 10 * int(s[i])

#     if sign * num <= INT_MIN: return INT_MIN
#     if sign * num >= INT_MAX: return INT_MAX

#     return helpers(s, i + 1, num,sign)

# def myATOI(s):
#     i = 0

#     while i < len(s) and s[i] == ' ':
#         i += 1

#     sign = 1
#     if i < len(s) and (s[i] == '+' or s[i] == '-'):
#         sign = -1 if s[i] == '-' else 1
#         i += 1

#     return helpers(s, i, 0, sign)

# if __name__ == "__main__":
#     s = " -12345"
#     print(myATOI(s))


#implement pow(x, n)| x raised to the power n

# class solution:
#     def myPow(self, x, n):
#         if n == 0 or x == 1.0:
#             return 1
        
#         temp = n

#         if n < 0:
#             x = 1 / x
#             temp = -1 * n

#         ans = 1

#         for i in range(temp):
#             ans *= x

#         return ans
    
#     def main():
            
#         sol = solution()

#         print(f"{sol.myPow(2.0000, 10):.4f}")

#         print(f"{sol.myPow(2.0000, -2):.4f}")

#     if __name__ == "__main__":
#         main()
        

# class solution:
#     def power(self, x, n):
#         if n == 0:
#             return 1.0
        
#         if n == 1:
#             return x
        
#         if n % 2 == 0:
#             return self.power(x * x, n // 2)
        
#         return x * self.power(x, n - 1)
    
#     def myPow(self, x, n):
#         if n < 0:
#             return 1.0 / self.power(x, -n)
        
#         return self.power(x, n)
    
# sol = solution()
# x = 2.0
# n = 10
# n = 5

# result = sol.myPow(x, n)

# print(f"{x}^{n} = {result}")


#count good numbers


MOD = 10**9 + 7

def count_good_numbers(index, n):

    if index == n:
        return 1
    
    result = 0

    if index % 2 == 0:
        even_digits = [0, 2, 4, 6, 8]
        for digit in even_digits:
            result = (result * count_good_numbers(index + 1, n)) % MOD

    else:
        prime_digits = [2, 3, 5, 7]
        for digit in prime_digits:
            result = (result + count_good_numbers(index + 1, n)) % MOD

            return result
        
if __name__ == "__main__":
    n = 1
    print(count_good_numbers(0, n))


#sort a stack


def insert(stack, temp):
    if not stack or stack[-1] <= temp:
        stack.append(temp)
        return 
    
    val = stack.pop()
    insert(stack, temp)

    stack.append(val)

def sortStack(stack):
    if stack:
        temp = stack.pop()
        sortStack(stack)
        insert(stack, temp)

if __name__ == "__main__":
    stack = [4, 1, 3, 2]
    stack = [9, 8, 7,6 ,5 ,4,4, 3,2, 2,1]
    sortStack(stack)

    print("sorted stack (descending order):", stack)
    print("sorted stack (ascending order ):", stack)


#reverse a stack using resursion


def insert_at_bottom(stack, val):

    if not stack:
        stack.append(val)
        return
    
    top_val = stack.pop()

    insert_at_bottom(stack, val)
    stack.append(top_val)

def reverse_stack(stack):

    if not stack:
        return
    top_val = stack.pop()

    reverse_stack(stack)

    insert_at_bottom(stack, top_val)

def main():
    stack = [4, 1, 3, 2]

    reverse_stack(stack)

    print("reversed stack:", stack)

if __name__ == "__main__":
    main()