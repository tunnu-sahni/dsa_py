#count reverse pairs

# from typing import List
# def countPairs(a: List[int], n: int) -> int:
#     cnt = 0
#     for i in range(n):

#         for j in range(i + 1, n):
#             if a[i] >  a[j]:
#                 cnt += 1
#     return cnt

# def team(skill: List[int], n: int) -> int:
#     return countPairs(skill, n)

# if __name__ == "__main__":
#     a = [4, 1, 2, 3, 1]
#     n = 5
#     n = 3
#     cnt = team(a, n)

#     print("the number of inversions are:", cnt)


# #count inversion in an array

# def number_of_inversions(arr):
#     cnt = 0

#     for i in range(len(arr)):

#         for j in range(i+1, len(arr)):

#             if arr[i] > arr[j]:
#                 cnt += 1

#     return cnt
# arr = [5, 4, 3, 2, 1]
# inversions = number_of_inversions(arr)

# print("the number of inversions is:", inversions)

# from typing import List

# def merge(arr, low, mid, high):

#     temp = []

#     left = low
#     right = mid + 1
    

#     while left <= mid and right <= high:

#         if arr[left] <= arr[right]:
#             temp.append(arr[left])
#             left += 1

#         else:
#             temp.append(arr[left])
#             left += 1

#     while right <= high:

#                 temp.append(arr[right])
#                 right += 1
#     while right <= high:
#          temp.append(arr[right])
#          right += 1

#     for i in range(low, high + 1):
#             arr[i] = temp[i - low]
        
# def countPairs(arr, low, mid, high):
#     right = mid + 1
#     cnt = 0
#     if low >= high:
#           return cnt
#     mid = (low + high) // 2
#     cnt += merge(arr, low, mid)

#     cnt += merge(arr, mid + 1, high )
#     cnt += countPairs(arr, low, mid, high)
#     merge(arr, low, mid, high)

#     return cnt
# def team(skill: List[int], n: int) -> int:
#       return merge(skill, 0, n - 1)

# if __name__ == "__main__":
#       a = [4, 1, 2, 3, 1]
#       n = 5
#       cnt = team(a, n)

#       print("the number of reverse pair is:", cnt)
    