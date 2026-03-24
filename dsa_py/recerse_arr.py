#reverse a given array

class solution:
    def reverseArray(self, arr):

        n = len(arr)

        ans = [0] * n

        for i in range(n):
            ans[i] = arr[n - 1 - i]

        return ans
    
if __name__ == "__main__":
    obj = solution()

    arr = [1,2,3,4,5]

    result = obj.reverseArray(arr)

    print("Reversed Array:", result)


class solution:
    def reverseArray(self, arr):
        p1 = 0
        p2 = len(arr) - 1
        while p1 < p2:
            arr[p1], arr[p2] = arr[p2], arr[p1]
            p1 += 1
            p2 -= 1

if __name__ == "__main__":
    sol = solution()

    arr = [1,2,3,4,5]

    sol.reverseArray(arr)
    print(" ". join(map(str, arr)))


class solution:
    def reverseArray(self, arr):
        arr[:] = arr[::-1]

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    obj = solution()
    obj.reverseArray(arr)

    print(" ".join(map(str, arr)))