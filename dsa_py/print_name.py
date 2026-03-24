#print name N times using recursion

class solution:
    def printName(self, name, count, N):
        if count == N:
            return
        print(name)

        self.printName(name, count + 1, N)

if __name__ == "__main__":
    sol = solution()
    N = 5
    N = 3
    N = 1
    name = "tunnu"
    sol.printName(name, 0, N)


# print 1 to using recursion

class solution:
    def printNumber(self, current, n):

        if current > n:
            return
        
        print(current, end='')

        self.printNumber(current + 1, n)

if __name__ == "__main__":
    sol = solution()
    n = 10

    sol.printNumber(1, n)
    print()


class solution:
    def printNumbers(self, current, n):

        if current > n:
            return
        
        self.printNumbers(current +1, n)

        print(current, end='')

if __name__ == "__main__":
    sol = solution()
    n = 10

    sol.printNumbers(1, n)
    print()