def sum_iterative(arr):
    total = 0
    for num in arr:
        total += num
    return total
num = [1,2,3,4,5]
print(num)


#sum array recursive 

def sum_recursive(arr):
    if not arr:
        return 0
    return arr[0] + sum_recursive(arr[1:])


#revrese string

def reverse_string(s):
    reverse_string = ""
    for char in s:
        reverse_string = char + reverse_string

    return reverse_string

#reverse string recursive

def recursive_string(s):
    if len(s) <= 1:
        return s
    return recursive_string(s[1:]) + s[0] 

#factorial loop

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i

    return result 

#factorial recursive

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    
    return n * factorial_recursive(n-1)

