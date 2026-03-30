def upper_bound(arr, target):
    left = 0
    right = len(arr) - 1
    ans = len(arr)

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] > target:
            ans = mid
            right = mid - 1

        else:
            left = mid + 1

    return ans

arr = [1,2,4,4,5,6]
print(upper_bound(arr, 6))

def upper_bound(arr, target):
    left = 0
    right = len(arr) - 1
    ans = len(arr)

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] > target:
            ans = mid
            right = mid - 1

        else:
            left = mid + 1
    return ans

arr = [1, 2, 3, 4, 5]
print(upper_bound(arr, 3))