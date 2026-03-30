# class LowerBoundFinder:

#     def lower_bound(self, arr, x):

#         for i in range(len(arr)):

#             if arr[i] >= x:
#                 return i
            
#         return len(arr)
    
# arr = [3, 5, 8, 15, 19]
# x = 9
# x = 4

# finder = LowerBoundFinder()
# ind = finder.lower_bound(arr, x)

# print("the lower bound is the index:", ind)


class LowerBoundFinder:

    def lower_bound(self, arr, x):

        for i in range(len(arr)):

            if arr[i] >= x:
                return i
            
        return len(arr)
arr = [4, 6, 2, 8, 10, 34]

x = 5
finder = LowerBoundFinder()

ind = finder.lower_bound(arr, x)

print("the lower bound is the index:", ind)



class LowerBoundFinder:
    def lower_bound(self, arr, x):
        low, high = 0, len(arr) - 1

        ans = len(arr)

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] >= x:
                ans = mid
                high = mid - 1

            else:
                low = mid + 1
        return ans
    

arr = [3, 5, 8, 15, 19]
x = 9

finder = LowerBoundFinder()
ind = finder.lower_bound(arr, x)

print("the lower bound is the index:", ind)