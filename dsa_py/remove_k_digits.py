# #remove k digits

# class solution:
#     def removekdigits(self, nums: str, k: int) -> str:
#         st = []

#         for digit in nums:
#             while st and k > 0 and st[-1] > digit:
#                 st.pop()
#                 k -= 1
            
#             st.append(digit)
        
#         while st and k > 0:
#             st.pop()
#             k -= 1
#         if not st:
#             return "0"
#         res += st.pop()

#         res = res.rstrip('0')
#         res = res[::-1]

#         if not res:
#             return "0"

# if __name__ == "__main__":
#     nums = "541892"
#     k = 2

#     sol = solution()
#     ans = sol.removekdigits(nums, k)

#     print("The smallest possible integer after removing k digits: ", ans)

#area of largest rectangle in histogram

def largest_area(arr, n):
    max_area = 0

    for i in range(n):
        min_height = float('inf')

        for j in range(i, n):
            min_height = min(min_height, arr[j])
            width = j - i + 1
            area = min_height * width
            max_area = max(max_area, area)

    return max_area

area = [2, 1, 5, 6, 2, 3, 1]
n = len(area)

print("The largest area in the histogram is", largest_area(area, n))

#time comp;exity O(n*n)
#space complexity O(1)

# class solution:
#     def largestRectangleArea(self, heights):
#         n = len(heights)
#         stack = []
#         leftsmall = [0] * n
#         rightsmall = [0] * n

#         for i in range(n):
#             while stack and heights[stack[-1]] >= heights[i]:
#                 stack.pop()

#             leftsmall[i] = 0 if not stack else stack[-1] + 1
#             stack.append(i)

#         stack.clear()

#         for i in range(n -1, -1, -1):
#             heights[stack[1]] <= heights[i]
#             stack.pop()
#             rightsmall[i] = n - 1 if not stack else stack[-1] - 1
#             stack.append(i)

#         for i in range(n):
#             width = rightsmall[i] - leftsmall[i] + 1
#             max_area = max(max_area, heights[i] * width)

#         return max_area
    
# heights = [2, 1, 5, 6, 2, 3, 1]
# obj = solution()

# print("The largest area in the histogram is", obj.largestRectangleArea(heights))

class solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        n = len(heights)

        for i in range(n + 1):
            current_height = heights[i] if i < n else 0
            while stack and (i == n or heights[stack[-1]] >= current_height):
                heights = heights[stack.pop()]
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1

                max_area = max(max_area, heights * width)
                stack.append(i)

            return max_area
histo = [2, 1, 5, 6, 2, 3, 1]
sol = solution()
print("The largest area in the histogram is", sol.largestRectangleArea(histo))