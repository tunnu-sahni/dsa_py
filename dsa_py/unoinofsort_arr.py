#union of two sorted arrays

# class solution:
#     def FindUnion(self, arr1, arr2, n, m):
#         freq = {}
#         for i in range(n):
#             freq[arr1[i]] = freq.get(arr1[i], 0) + 1
#         for i in range(m):
#             freq[arr2[i]] = freq.get(arr2[i], 0) + 1
#             Union = sorted(freq.keys())
#             return Union
        
# if __name__ =="__main__":
#     n = 10
#     m = 7
#     arr1 = [1,2,3,4,5,6,7,8,9,10]
#     arr2 = [2,3,4,4,5,11,12]
#     obj = solution()
#     Union = obj.FindUnion(arr1,arr2,n,m)
#     print("Union of arr1 and arr2 is")
#     print(*Union)


# class solution:
#     def findUnion(self, arr1, arr2):
#         st = set(arr1) | set(arr2)
#         return sorted(st)
    
# arr1 = [1,2,3,4,5,6,7,8,9,10]
# arr2 = [2,3,4,4,5,11,12]

# obj = solution()
# result = obj.findUnion(arr1, arr2)

# print("Union of arr1 and arr2 is:", *result)


class solution:
    def findUnion(self,arr1, arr2, n, m):
        Union = []
        i, j = 0,0

        while i < n and j < m:
            if arr1[i] < arr2[j]:
                if not Union or Union[-1] != arr1[i]:
                    Union.append(arr1[i])
                    i += 1

                elif arr2[j] < arr1[i]:
                    if not Union or Union[-1] != arr2[j]:
                     Union.append(arr2[j])
                    j += 1
                else:
                    if not Union or Union[-1] != arr1[i]:
                        Union.append(arr1[i])
                        i += 1
                        j += 1
        while i < n:
            if not Union or Union[-1] != arr1[i] != arr1[i]:
                Union.append(arr1[i])
                i += 1
        while j < m:
            if not Union or Union[-1] != arr2[j]:
                Union.append(arr2[j])
                j += 1

        return Union
    
if __name__ == "__main__":
    arr1 = [1,2,3,4,5,6,7,8,9,10]
    arr2 = [2,3,4,4,5,11,12]
    n, m = len(arr1), len(arr2)

    obj = solution()
    result = obj.findUnion(arr1, arr2, n, m)
    print("Union of arr1 and arr2 is" , *result)

                      