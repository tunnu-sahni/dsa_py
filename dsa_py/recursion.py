class solution:

    def printName(self, name, count, N):
        if count == N:
            return
        
        print(name)
        # print(count)
        # print(N)

        self.printName(name, count + 1, N)

if __name__ == "__main__":
    sol = solution()
    N = 5
    N = 3
    N = 1
    name = "tunnu"

    sol.printName(name, 0, N) 