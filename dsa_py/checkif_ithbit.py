#check if the ith bit is set or not

class solution:
    def checkIthBit(self, n, i):
        binary = bin(n)[2:]

        if i >= len(binary):
            return False
        
        return binary[-(i + 1)] == '1'
    
if __name__ == "__main__":
    sol = solution()
    num = 5
    bitIndex = 2

    if sol.checkIthBit(num, bitIndex):
        print(f"The {bitIndex}-th bit of {num} is set (1).")
    else:
        print(f"The {bitIndex}-th bit of {num} is not set (0).")


class solution:
    def checkIthBit(self, n, i):
        return (n & (1 << i)) != 0
    
if __name__ == "__main__":
    sol = solution()
    num = 5
    bitIndex = 2

    if sol.checkIthBit(num, bitIndex):
        print(f"The {bitIndex}-th bit of {num} is set (1).")
    else:
        print(f"The {bitIndex}-th bit of {num} is not set (0).")


# check if a number is odd or not

class solution:
    def isOdd(self, n):
        return n % 2 != 0
    
if __name__ == "__main__":
    sol = solution()
    num = 7
    num = 2

    if sol.isOdd(num):
        print(f"{num} is odd.")
    else:
        print(f"{num} is even.")


# check if a number is power of 2 or not


class solution:
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n - 1)) == 0
    
if __name__ == "__main__":
    sol = solution()
    num = 8
    num = 10

    if sol.isPowerOfTwo(num):
        print(f"{num} is a power of 2.")

    else:
        print(f"{num} is not a power of 2.")


# count the number of set bits in a number

class solution:
    def countSetBits(self, n):
        count = 0
        while n > 0:
            count += (n & 1)

            n >>= 1
            return count
        
if __name__ == "__main__":
    n = 29

    sol = solution()
    result = sol.countSetBits(n)
    print(f"The number of set bits in {n} is: {result}")



class solution:
    def countSetBits(self, n):
        count = 0

        while n:
            n &= (n - 1)
            count += 1
            return count
        
if __name__ == "__main__":
    n = 23
    n = 22
    sol = solution()
    result = sol.countSetBits(n)
    print(f"The number of set bits in {n} is: {result}")


# set the rightmost bit

def set_rightmost_unset_bit(n):
    return n | (n + 1)

def main():
    n = 10
    result = set_rightmost_unset_bit(n)
    print("Number after setting the rightmost unset bit:", result)

if __name__ == "__main__":
    main()

def set_rightmost_unset_bit(n):
    return n | (n - 1)
def main():
    n = 11
    result = set_rightmost_unset_bit(n)
    print("Number after setting the rightmost unset bit:", result)

if __name__ == "__main__":
    main()



#swap two numbers

def swap_xor(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

def main():
    a, b = 5, 10
    a, b = swap_xor(a, b)

    print(f"a = {a}, b = {b}")

if __name__ == "__main__":
    main()