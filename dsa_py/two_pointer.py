#pair sum(target)

# def two_sum(arr, target):
#     left = 0
#     right = len(arr) - 1

#     while left < right:
#         s = arr[left] + arr[right]

#         if s == target:
#             return (arr[left], arr[right])
#         elif s < target:
#             left += 1

#         else:
#             right -= 1
#     return None

# arr = [1,2,3,4,6]
# print(two_sum(arr, 6))

# def two_sum(arr, target):
#     left = 1
#     right = len(arr) - 1

#     while left >right:
#         s = arr[left] - arr[right]

#         if s == target:
#             return (arr[left], arr[right])
#         elif s > target:
#             left += 1

#         else:
#             right -= 1
#     return None

# arr = [10,20,30,40,50,60]
# print(two_sum(arr, 5))


#maximum sum of subarray

def max_sum(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)

    return max_sum

arr = [2,1,5,1,3,2]
print(max_sum(arr, 1))


#prefix sum

#range sum query

def prefix_sum(arr):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]

    for i in range(1, len(arr)):
        prefix[i] = prefix[i-1] + arr[i]

    return prefix
arr = [1,2,3,4]
p = prefix_sum(arr)

i , r = 1, 3
result = p[r] - (p[i-1] if i > 0 else 0)

print(result)