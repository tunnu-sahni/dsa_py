#find the largest element in an array


# def sortArr(arr):
#     arr.sort()

#     return arr[-1]

# if __name__ == "__main__":
#     arr1 = [2, 5, 1, 3, 0]
#     arr2 = [8, 10, 5, 7, 9]

#     print("the largest element in the arr is:", sortArr(arr1))
#     print("the largest element in the array is:", sortArr(arr2))


def findLargestElement(arr, n):
    max = arr[0]

    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max

if __name__ == "__main__":
    arr1 = [2, 5, 1, 3, 0]
    n = len(arr1)
    max = findLargestElement(arr1, n)
    print("the largest element in the arr is:", max)

    arr2 = [8, 10, 5, 7, 9]
    n = len(arr2)
    max = findLargestElement(arr2, n)
    print("the largest element in the array is:", max)