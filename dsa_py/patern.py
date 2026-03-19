# class solution:
#     def pattern(self, H):
#         for i in range(H):
#             for j in range(H - i - 1):
#                 print(" ",end=" ")
#             for j in range(2 * i + 1):
#                 print("*", end="")
                

# if __name__ == "__main__":
#     sol = solution()
#     H = 3
#     sol.pattern(H)



# class solution:
#     def erect_pyramid(self,N):
#         for i in range(N):
#             print(""*(N-i-1),end="")

#             print(""*(N - i -1))

#     def inverted_pyramid(self,N):
#         for i in range(N):
#             print(" "*i, end="")
#             print("*"*(2*N-(2*i+1)),end="")
#             print(" " * i)

#     if __name__ == "__main__":
#         N = 5
#         obj = solution()
#         obj.erect_pyramid(N)
#         obj.inverted_pyramid(N)


# class solution:
#     def pattern(self,N):
#         spaces = 2 *(N - 1)

#         for i in range(1, N + 1):
#             for j in range(1, i + 1):
#                 print(j, end=" ")
#                 for j in range(1, spaces + 1):
#                     print(" ", end="")
#                     for j in range(i, 0, -1):
#                         print(j, end="")
#                         print()
#                         spaces -= 2
# sol = solution()
# # N = 5
# # N = 3
# N = 6
# sol.pattern(N)



# class solution:
#     def pattern(self,N):
#         num = 1
#         for i in range(1, N + 1):
#             for j in range(1, i + 1):
#                 print(num, end=" ")
#                 num += 1
#                 print()

# sol = solution()
# N = 5
# N = 3
# N = 6
# sol.pattern(N)


# class solution:
#     def pattern(self,N):
#         for i in range(N):
#             for j in range(i + 1):
#                 print(chr(65 + j), end=" ")
#                 print()

# sol = solution()
# N  = 5
# N = 3
# N = 6
# sol.pattern(N)



class solution:
    def pattern(self,N):
        for i in range(N):
            for j in range(i + 1):
                print(chr(65 + i), end=" ")
                print()

sol = solution()
N = 5
N = 3
sol.pattern(N)



class solution:
    def pattern(self, n):
        for i in range(n):
            for j in range(n):
                if i == 0 or j == 0 or i ==n - 1 or j == n - 1:
                    print("*", end=" ")
                else:
                    print()

if __name__ == "__main__":
    sol = solution()
    n = 5
    n = 3
    n = 6
    sol.pattern(n)
                    


