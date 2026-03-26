#find the missing number

# def missingNum(arr):
#     n = len(arr) + 1

#     for i in range(1, n + 1):
#         found = False
#         for j in range(n - 1):
#             if arr[j] == i:
#                 found = True
#                 break

#         if not found:
#             return i
#     return -1

# if __name__ == '__main__':
#     arr = [8, 2, 4, 5, 3, 7, 1]

#     print(missingNum(arr))



# def missingNum(arr):
#     n = len(arr) + 1
#     hash = [0] * (n + 1)

#     for i in range(n - 1):
#         hash[arr[i]]  += 1

#     for i in range(1, n + 1):
#         if hash [i] == 0:
#             return 1
    
#     return - 1

# if __name__ == '__main__':
#     arr = [8, 2, 4, 5, 3, 7, 1]
#     res = missingNum(arr)
#     print(res)



def missingNum(arr):
    n = len(arr) + 1

    totalSum = sum(arr)

    expSum = n * (n + 1) // 2

    return expSum - totalSum

if __name__ == '__main__':
    arr = [4, 5,76,2,7,4]

    print(missingNum(arr))


def missingNum(arr):
    n = len(arr) + 1
    xor1 = 0
    xor2 = 0

    for i in range(n - 1):
        xor2 ^= arr[i]

    for i in range(1, n + 1):
        xor1 ^= i

    return xor1 ^ xor2

if __name__ == '__main__':
    arr = [8, 2, 4, 5, 3, 7, 1]
    res = missingNum(arr)
    print(res)