# arr = [1,2 ,4, 5, 6, 7, 8, 9]
# target = 5
# for i in range(len(arr)):
#     if arr[i] == target:
#         print(i)
#         print(arr[i])
#         break

#     #  arr[i] = arr[3] = 5


# arr = [1,2,5,6,7]
# target = 6
# for i in range(len(arr)):
#     if arr[i] == target:
#         print(i)
#         print(arr[i])
#         break 


# arr = [2,5,22,54,64]
# target = 5
# for i in range(len(arr)):
#     if arr[i] == target:
#         print(i)
#         print(arr[i])
#         break 



# arr = [3,4,5,32,76]
# target = 76
# for i in range (len(arr)):
#     if arr[i] == target:
#         print(i)
#         print(arr[i])
#         break

# class solution:
#     def pattern1(self, arr, target):
#         for i in range(N):
#             for j in range(N):
#                 print("*", end="")
#                 print()
# sol = solution()
# N = 5
# sol.pattern1(arr, target)


# class solution:
#     def pattern2(self, arr, target):
#         for i in range(T):
#             print("*" *(i+1))

# if __name__ == "__main__":
#     sol = solution()
#     T = 5
#     sol.pattern2(arr, target)



# class solution:
#     def pattern3(self, arr, S):

#         for i in range(S):
#             for i in range(1, S+1):
#                 for j in range(1, i+1):
#                     print(j, end="")
#                     print()
# if __name__ == "__main__":
#     sol = solution()
#     S = 4
#     sol.pattern3(arr, S)



# class solution:
#     def pattern4(self, F):
#         for i in range(2, F+1):
#             for j in range(1, i+1):
#                 print(i, end="")
#                 print()

# if __name__ == "__main__":
#     sol = solution()
#     F = 5 
#     sol.pattern4(F)



class solution:
    def pattern5(self, N):
        for i in range(N):
            for j in range(N, i, -1):
                print("*", end=" ")
                print()

if __name__ == "__main__":
    sol = solution()
    N = 3
    sol.pattern5(N)