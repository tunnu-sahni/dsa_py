# # #number of NGE to the right

# # class solution:
# #     def nextgreaterElement(self, arr):
# #         n = len(arr)
# #         ans = [-1] * n
# #         stack = []

# #         for i in range(n):
# #             currEle = arr[i]

# #             for j in range(i + 1, n):
# #                 if arr[j] > currEle:
# #                     ans[i] = arr[j]
# #                     break

# # if __name__ == "__main__":
# #     n = 4
# #     arr = [1, 3, 2, 4]
# #     sol = solution()

# #     ans = sol.nextgreaterElement(arr)
# #     print("The next greater elements are: ")

# #     for i in range(len(ans)):
# #         print(ans[i], end=" ")

# # class solution:
# #     def nextgreaterElement(self, arr):
# #         n = len(arr)
# #         ans = [-1] * n
# #         stack = []

# #         for i in range(n):
# #             currEle = arr[i]

# #         for j in range(i + 1, n):
# #             if arr[j] > currEle:
# #                 ans[i] = arr[j]
# #                 break
# #         return ans
    
# # if __name__ == "__main__":
# #     n = 4
# #     arr = [1, 3, 2, 4]
# #     sol = solution()

# #     print("The next greater elements are: ")

# #     for i in range(len(ans)):
# #         print(ans[i], end=" ")

# # def nextGreaterElement(arr):
# #     n = len(arr)
# #     result = [-1] * n
# #     stack = []

# #     for i in range(n - 1, -1, -1):
# #         while stack and stack[-1] <= arr[i]:
# #             stack.pop()

# #         if stack:
# #             result[i] = stack[-1]

# #         stack.append(arr[i])

# #     return result   # 🔥 IMPORTANT

# # # Main code
# # arr = [4, 5, 2, 10, 8]
# # ans = nextGreaterElement(arr)

# # print("The next greater elements are:")
# # for i in range(len(ans)):
# #     print(ans[i], end=" ")

# #asteroid collision

# class solution:
#     def asteroidCollosion(self, asteroida):
#         n = len(self.asteroidCollosion)
#         st = []

#         for i in range(n):
#             if self.asteroidCollosion[i] > 0:
#                 st.append(self.asteroidCollosion[i])

#             else:
#                 while (st and st[-1] > 0  and st[-1] < abs(self.asteroidCollosion[i])):

#                     st.pop()

#                 if st and st[-1] == abs(self.asteroidCollosion[i]):
#                     st.pop()


#                 elif not st or st[-1] < 0:
#                     st.append(self.asteroidCollosion[i])

#             return st
# if __name__ == "__main__":
#     arr = [10, 20, -10] 
#     sol = solution()

#     ans= sol.asteroidCollosion
#     print("The state of asteroids after collisions is: ", ans)

#     for i in range(len(arr)):
#         print(arr)


# #sum of subarray range

# class solution:
#     def subArrayRanges(self, arr):
#         n = len(arr)
#         total_sum = 0

#         for i in range(n):
#             smallest = arr[i]
#             largest = arr[i]

#             for j in range(i, n):
#                 smallest = min(smallest, arr[j])

#                 largest = max(largest, arr[j])

#                 total_sum += (largest - smallest)
#             return total_sum
        
# if __name__ == "__main__":
#     arr = [1, 2, 3]
#     sol = solution()
#     ans = sol.subArrayRanges(arr)

#     print("The sum of subarray ranges is: ", ans)

# class solution:
#     def findNSE(self, arr):
#         n = len(arr)
#         ans = [0] * n
#         st = []

#         for i in range(n - 1, -1, -1):
#             currEle = arr[i]

#             while st and arr[st[-1]] >= currEle:
#                 st.pop()
            
#             ans[i] = st[-1] if st else n
#             st.append(i)
#         return ans
    
#     def findNSE(self, arr):
#         n = len(arr)
#         ans [0] * n
#         st = []
#         for i in range(n -1, -1, -1):
#             currEle = arr[i]

#             while st and arr[st[-1]] <= currEle:
#                 st.pop()
#                 st.append(i)
#             return ans
#     def findNSE(self, arr):
#         n = len(arr)
#         ans = [0] * n
#         st = []

#         for i in range(n):
#             currEle = arr[i]
#             while st and arr[st[-1]] > currEle:
#                 st.pop()
#             ans[i] = st[-1] if st else -1
#             st.append(i)

#         return ans
#     def findNSE(self, arr):
#         n = len(arr)
#         ans = [0] * n
#         st = []

#         for i in range(n):
#             currEle = arr[i]
#             while st and arr[st[-1]] < currEle:
#                 st.pop()
#                 ans[i] = st[-1] if st else -1

#                 st.append(i)

#             return ans
#         def sunSubarrayMins(self, arr):
#             nse = self.findNSE(arr)
#             psee = self.findPSEE(arr)

#             n = len(arr)
#             total_sum = 0

#             for i in range(n):
#                 left = i - psee[i]
#                 right = nse[i] -i
#                 freq = left * right * 1

#                 val = (freq * arr[i] * 1)
#                 total_sum += val
#             return total_sum
    
# if __name__ == "__main__":
#     arr = [1, 2, 3]
#     sol = solution()
#     ans = sol.subArrayRanges(arr)
#     print("The sum of subarray ranges is: ", ans)