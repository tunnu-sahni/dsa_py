#last occurance in a sorted array

# def solve(n: int, key: int, v: list[int]) -> int:
#     res = -1

#     for i in range(n - 1, -1, -1):
#         if v[i] == key:
#             res = i
#     return res

# def main():

#     n = 7
#     key = 13

#     v = [3, 4, 13, 13, 13, 20, 40]
#     print(solve(n, key, v))

# if __name__ == "__main__":

#  if __name__ == "__main__":
#     main()

#time complexity: O(N)
#space complexity: O(1)



def solve(n: int, key: int, v: list[int]) -> int:
   
   start, end, res = 0, n - 1, -1

   while start <= end:
      
      mid = start + (end - start) // 2

      if v[mid] == key:
         res = mid
         start = mid + 1

      elif key < v[mid]:
         end = mid - 1

      else:
         start = mid + 1

      return res
   
def main():
   
   n = 7
   key = 13

   v = [3, 4, 13, 13, 13, 20, 40]

   print(solve(n, key, v))

   if __name__ == "__main__":
      main()

    #time complexity: O(log N)
    #space complexity: O(1)
    