#next greater element

# class solution:
#     def nextGreater(self, nums):
#         stack = []

#         n = len(nums)
#         res = [0] * n

#         for i in range(n - 1, -1, -1):
#             while stack and stack[-1] <= nums[i]:
#                 stack.pop()

#             if not stack:
#                 res[i] = -1

#             else:
#                 res[i] = stack[-1]

#             stack.append(nums[i])

#         return res
    
# def main():
#     nums = [4, 5, 2, 10]
#     sol = solution()
#     ans = sol.nextGreater(nums)
#     print(" ".join(map(str, ans)))

# main()

# #time complexity O(N)
# #space complexity O(N)

# class solution:
#     def nextGreater(self, nums):
#         stack = []
#         n = len(nums)
#         res = [0] * n

#         for i in range(n - 1, -1, -1):
#             while stack and stack[-1] <= nums[i]:
#                 stack.pop()

#             if not stack:
#                 res[i] = -1

#             else:
#                 res[i] = stack[-1]

#             stack.append(nums[i])

#         return res
    
# def main():
#     nums = [5, 10, 4, 29, 34]
#     sol = solution()
#     ans = sol.nextGreater(nums)
#     print(" ".join(map(str, ans)))

# main()

#next greater element-2

# class solution:
#     def nextGreaterElement(self, arr):
#         n = len(arr)
#         ans = [-1] * n

#         for i in range(n):
#             currEle = arr[i]

#             for j in range(1, n):
#                 ind = (j + i) % n

#                 if arr[ind] > currEle:
#                     ans[i] = arr[ind]
#                     break

#         return ans
        
# if __name__ == "__main__":
#     n = 6
#     arr = [5, 7, 1, 7, 6, 0]
#     sol = solution()
#     ans = sol.nextGreaterElement(arr)
#     print("The next greater element are: ", end=" ")

#     for i in range(n):
#         print(ans[i], end=" ")

# #tiem complexity O(N2)
# #space complexity O(n)

# class solution:
#     def nextGreaterElement(self, arr):
#         n = len(arr)
#         ans = [-1] * n

#         st = []
#         for i in range(2 * n - 1, -1, -1):
#             ind = i % n
#             currEle = arr[ind]

#             while st and st[-1] <= currEle:
#                 st.pop()

#             if i < n:
#                 if st:
#                     ans[i] = st[-1]
#             st.append(currEle)

#         return ans
# if __name__ == "__main__":
#     arr = [5, 7, 1, 7, 6, 0]
#     sol = solution()
#     ans = sol.nextGreaterElement(arr)
#     print("The next greater element are: ", ans)
# #time compl;exity O(n)
# #space complexity O(n)

# #next smaller element

# class solution:
#     def nextgreaterElement(self, arr):
#         n = len(arr)
#         ans = [-1] * n

#         for i in range(n):
#             for j in range(i + 1, n):
#                 if arr[j] < arr[i]:
#                     ans[i] = arr[j]
#                     break
#         return ans
    
# arr = [1, 3, 2, 4]
# sol = solution()
# ans = sol.nextgreaterElement(arr)
# print("The next smaller element are:", *ans)

#time complexity O(N^2)
#space c O(n)

class solution:
    def nextGreaterElement(self, arr):
        n = len(arr)
        st = []
        ans = [-1] * n
        for i in range(n - 1, -1, -1):
            while st and st[-1] >= arr[i]:
                st.pop()
            if st:
                ans[i] = st[-1]
            
            st.append(arr[i])

        return ans
    
arr = [1, 3, 2, 4]
sol = solution()
ans = sol.nextGreaterElement(arr)

print("The next greater element are: ", *ans)