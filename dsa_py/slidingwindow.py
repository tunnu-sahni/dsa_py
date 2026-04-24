# #find the longest substring without repeating charactors

# def longest_subtring(s):
#     char_set = set()
#     left = 0
#     max_len = 0

#     for right in range(len(s)):
#         while s[right] in char_set:
#             char_set.remove(s[left])
#             left += 1

#         char_set.add(s[right])
#         max_len = max(max_len, right - left + 1)

#     return max_len
# print(longest_subtring("abcabcbb"))
# print(longest_subtring("bbbbb"))



# #max consecutive once 

# class solution:
#     def longestOnes(self, nums, k):
#         max_len = 0
#         for i in range(len(nums)):
#             zeros = 0
#             for j in range(i, len(nums)):
#                 if nums[j] == 0:
#                     zeros += 1

#                     if zeros > k:
#                         break
#                     max_len = max(max_len, j - i + 1)

#         return max_len
    
# if __name__ == "__main__":
#     sol = solution()
#     nums = [1,1,1,0,0,0,1,1,1,1,0]
#     k = 2
#     print(sol.longestOnes(nums, k))


class solution:
    def longestOnes(self, nums, k):
        left = 0
        zeros = 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                    left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

if __name__ == "__main__":
    sol = solution()
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    print(sol.longestOnes(nums, k))

class solution:
    def longestOnes(self, nums, k):
        left = 0
        zeroscount = 0
        maxlen = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroscount += 1

                if zeroscount > k:
                    if nums[left] == 0:
                        zeroscount -= 1
                    left += 1
                maxlen = max(maxlen, right - left + 1)

        return maxlen
    
if __name__ == "__main__":
    sol = solution()
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2

    print(sol.longestOnes(nums, k))
          
          
          
          
          
          
          
          
          
        