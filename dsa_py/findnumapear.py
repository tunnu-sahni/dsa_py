#find the number that appears once and the other numers twice

class solution:
    def getSingleElement(self, arr):
        n = len(arr)

        for i in range(n):
            num = arr[i]
            count = 0

            for j in range(n):
                if arr[j] == num:
                    count += 1

            if count == 1:
                return num
        return - 1
    
arr = [4, 1, 2, 1, 2]
obj = solution()
ans = obj.getSingleElement(arr)

print("the single element is:", ans)


class solution:
    def getSingleElement(self, arr):
        n = len(arr)

        maxi = max(arr)

        hash_arr = [0] * (maxi + 1)

        for num in arr:
            hash_arr[num] += 1

            for num in arr:
                if hash_arr[num] == 1:
                    return num
        return - 1
    
arr = [4, 1, 2, 1, 2]
obj = solution()
ans = obj.getSingleElement(arr)
print("the single element is:", ans)


class solution:
    def getSingleElement(self, arr):
        xor = 0

        for num in arr:
            xor ^= num
        return xor

arr = [4, 1, 2, 1, 2]
obj = solution()
ans = obj.getSingleElement(arr)
print("the single element is:", ans)        