#bubble sort

# def bubble_sort(arr):
#     n = len(arr)

#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

#     return arr
# print(bubble_sort([5,3,8,1]))


# def bubble_sort(arr):
#     s = len(arr)

#     for i in range(s):
#         for j in range(0, s-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

#     return arr
# print(bubble_sort([6,8,3,0,1]))



# selection

# def selection_sort(arr):
#     n = len(arr)

#     for i in range(n):
#         min_idx = i

#         for j in range(i+1, n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j

#         arr[i], arr[min_idx] = arr[min_idx], arr[i]

#     return arr

# print(selection_sort([5,3,8,1]))


# def selection_sort(arr):
#     n = len(arr)

#     for i in range(n):
#         mix_idx = i

#         for j in range(i+1, n):
#             if arr[j] > arr[mix_idx]:
#                 max_idx = j
#         arr[i], arr[mix_idx] = arr[mix_idx], arr[i]

#     return

# print(selection_sort([22,4,55,7,1,65]))


#insertion sort

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1

#         while j >= 0 and arr[j] > key:
#             arr[j+1] = arr[j]
#             j -= 1
        
#         arr[j+1] = key

#     return

# print(insertion_sort([5, 3, 8,1]))


#merge sort


# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) //2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])

#     return merge(left, right)

# def merge(left, right):
#     result = []
#     i = j = 0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1

#         else:
#             result.append(right[j])
#             j += 1

#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result

# print(merge_sort([5,3,8,1]))


#quick sort


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]

    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort([5,3,8,1]))
print(quick_sort([2,4,7,8,3]))


#built in sort

arr = [5,3,8,1]   

arr.sort()
print(arr)
print(sorted(arr))


