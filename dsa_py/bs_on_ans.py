#finding square of a number using binary search

import re
from unittest import result


class solution:
    def floorSqrt(self, n):
        low = 1
        high = n
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if mid * mid <= n:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans


#  object class ke bahar banao
sol = solution()

n = 28
print(sol.floorSqrt(n))

#time complexity: O(N)
#space complexity: O(1)



# class solution:
#     def mySqrt(self, x: int) -> int:
#         if x < 2:
#             return x
        
#         left, right, ans = 1, x //2, 0

#         while left <= right:
#             mid = (left + right) // 2

#             if mid * mid <= x:
#                 ans = mid
#                 left = mid + 1

#             else:
#                 right = mid - 1
#         return ans
#     if __name__ == "__main__":
#         s = solution()
#         print(s.mySqrt(8))

#     #time complexity: O(log(N))
#     #space complexity: O(1)



#Nth root of a number using binary search

# class solution:
#     def nthRoot(self, n, m):
#         for i in range(1, m + 1):

#             power = i ** n

#             if power == m:
#                 return i
            
#             if power > m:
#                 break

#         return i - 1
    
# sol = solution()
# n = 3
# m = 27

# print("Nth Root:", sol.nthRoot(n, m))

#time complexity: O(M)
#space complexity: O(1)

# class solution:
#     def nthRoot(self, n, m):
#         low, high = 1, m

#         while low <= high:
#             mid = (low + high) // 2
#             ans = 1

#             for _ in range(n):
#                 ans *= mid
#                 if ans > m:
#                     break

#             if ans < m:
#                 low = mid + 1

#             else:
#                 high = mid - 1

#         return - 1
    

# obj = solution()
# result = obj.nthRoot(3, 27)
# print("Nth Root:", result)

#time complexity: O(log(M))
#space complexity: O(1)



#minimum days to make m bouquets


# class RoseGarden:
#     def is_possible(self, bloom_days, day, m, k):
#          count = 0
#          bouquets = 0

#          for bloom in bloom_days:
#              if bloom <= day:
#                  count += 1
#              else:
#                  count = 0

#              if count == k:
#                  bouquets += 1
#                  count = 0

#          return bouquets >= m
    
#     def min_days_to_make_bouquets(self, bloom_days, m, k):
#         total_flowers  = m * k
#         if total_flowers > len(bloom_days):
#             return - 1
        
#         low = min(bloom_days)
#         high = max(bloom_days)

#         for day in range(low, high + 1):
#             if self.is_possible(bloom_days, day, m, k):
#                 return day
            
# bloom_days = [7, 7, 7, 7, 13, 11, 12, 7]
# k = 3
# m = 2

# garden = RoseGarden()
# result = garden.min_days_to_make_bouquets(bloom_days, m, k)

# if result == -1:
#     print("we cannot make m bouquets.")

# else:
#     print(f"we can make bounquets on day {result}")

# #time complexity: O(N * log(max(bloom_days)))
#space complexity: O(1)



class RoseGarden:
    def is_possible(self, bloom_days, day, m, k):
        count = 0
        bounquets = 0

        for bloom in bloom_days:
            if bloom <= day:
                count += 1
                if count == k:
                    bounquets += 1
                    count = 0
            else:
                count = 0
        return bounquets >= m
    
    def rose_garden(self, bloom_days, m, k):
        if m * k > len (bloom_days):
            return - 1
        
        low = min(bloom_days)
        high = max(bloom_days)
        answer = -1

        while low <= high:
            mid = (low + high) // 2

            if self.is_possible(bloom_days, mid, m, k):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        return answer
    
garden = RoseGarden()
bloom_days = [7, 7, 7, 7, 13, 11, 12, 7]
m = 3
k = 3

if result  == -1:
    print("we cannot make m bounquets.")

else:
    print(f"we can make bounquets on day {result}")


#time complexity:O(1)
#space complexity: O(h)O(1)