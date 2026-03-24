#sum of first N natural numbers

# class solution:

#     def sumOfNaturalNumbers(self, N):
#         total = 0

#         for i in range(1, N + 1):
#             total += i

#         return total
    
# if __name__ == "__main__":
#     obj = solution()
#     N = int(input())
#     result = obj.sumOfNaturalNumbers(N)
#     print(result)


# class solution:
#     def sumOfnaturalNumbers(self, N):
#         return (N * (N + 1)) //2
    
# if __name__ == "__main__":
#     obj = solution()
#     N = int(input())
#     print(obj.sumOfNaturalNumbers(N))



# class Solution:
#     def sumOfNaturalNumbers(self, N):
#         return N * (N + 1) // 2   # formula method


# # object create karo
# obj = Solution()

# # input value
# N = 10

# # function call
# print(obj.sumOfNaturalNumbers(N))


class solution:
    def sumOfNaturalNumbers(self, N):
        if N == 1:
            return 1
        return N + self.sumOfNaturalNumbers(N - 1)
if __name__ == "__main__":
    obj = solution()
    N = int(input())
    print(obj.sumOfNaturalNumbers(N))