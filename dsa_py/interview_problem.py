# #count number of bits to be flipped to convert A to B

# class solution:

#     def minBitsFlip(self, start, goal):

#         num = start ^ goal
#         count = 0

#         for i in range(32):
#             count += (num & 1)
#             num = num >> 1

#         return count
    
# if __name__ == "__main__":
#     start, goal = 10, 7
#     sol = solution()
#     ans = sol.minBitsFlip(start, goal)

#     print("The minimum bit flips to convert number is:", ans)


# #find the number that apperars once and the other numbers twice

# class solution:
#     def getSingleElement(self, arr):
#         n = len(arr)

#         for i in range(n):
#             num = arr[i]
#             count = 0

#             for j in range(n):
#                 if arr[j] == num:
#                     count += 1

#             if count == 1:
#                 return num
#         return -1
    
# arr = [4, 1, 2, 1, 2]
# obj = solution()
# ans = obj.getSingleElement(arr)

# print("The single element is:", ans)



# class solution:
#     def getSingleElement(self, arr):
#         n = len(arr)

#         maxi = max(arr)
#         hash_arr = [0] * (maxi + 1)

#         for i in arr:
#             hash_arr[i] += 1
#         for i in range(maxi + 1):
#             if hash_arr[i] == 1:
#                 return i
#         return -1
    
# arr = [12, 1, 2, 1, 2]
# obj = solution()
# ans = obj.getSingleElement(arr)
# print("The single element is:", ans)


# #power set | bit amnipulation

# class solution:
#     def getPowerset(self, nums):
#         n = len(nums)

#         subsets = 1 << n
#         ans = []
#         for num in range(subsets):
#             subset = []
#             for i in range(n):
#                 if num & (1 << i):
#                     subset.append(nums[i])
#             ans.append(subset)
#         return ans
    
#     if __name__ == "__main__":
#         nums = [5, 7, 8]
#         obj = solution()
#         subsets = obj.getPowerSet(nums)
#         print("The power array:", nums)
#         print("subset:")
#         for subset in subsets:
#             print("[", " ".join(map(str, subset)), "]")


#find xor of numbers from L to R

# class solution:
#     def findRangeXOR(self, l, r):
#         ans = 0
#         for i in range(1, r + 1):
#             ans ^= i
#         return ans
    
# if __name__ == "__main__":
#     l, r = 3, 5
#     sol = solution()
#     ans = sol.findRangeXOR(1, r)
#     print(f"the XOR of numbers from {1} to {r} is: {ans}")


#find the two numbers appearing odd number of times

# class solution:
#     def singleNumber(self, nums):
#         ans = []
#         mpp = {}
#         for num in nums:
#             mpp[num] = mpp.get(num, 0) + 1
#             for key, value in mpp.items():
#                 if value == 1:
#                     ans.append(key)
#                     ans.sort()
#                     return ans
                
# sol = solution()
# nums = [1, 2, 1, 3, 5, 2]
# ans = sol.singleNumber(nums)
# print("The single numbers in given array are:", ans[0], ans[1])


class solution:
    def singleNumber(self, nums):
        n = len(nums)
        ans = 0
        XOR = 0
        for i in range(n):
            XOR = XOR ^ nums[i]
            rightmost = (XOR & (XOR - 1)) ^ XOR
            XOR1, XOR2 = 0, 0
            for i in range(n):
                if nums[i] & rightmost:
                    XOR1 = XOR1 ^ nums[i]
                else:
                    XOR2 = XOR2 ^ nums[i]
            return [XOR1, XOR2] if XOR1 < XOR2 else [XOR1, XOR2]
        
nums = [1, 2, 1, 3, 5, 2]
sol = solution()
ans = sol.singleNumber(nums)
print("The single numbers in given array are:", ans[0], ans[1])