#count frequency of each element in the array

def countFreq(arr, n):
    visited = [False] * n

    for i in range(n):
        if visited[i]:
            continue
        count = 0
        count += 1
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                visited[j] = True

                count += 1

        print(arr[i], count)

if __name__ == "__main__":
    arr = [10,5,10,15,10,5,1,1,1,1,1,1]
    n = len(arr)

    countFreq(arr, n)
print(arr, n)


from collections import defaultdict

class solution:
    def Frequency(self, arr, n):
        freq_map = defaultdict(int)

        for i in range(n):
            freq_map[arr[i]] += 1

        for key, value in freq_map.items():
                       print(key, value)

if __name__ == "__main__":
     arr = [10,5,10,15,10,5,2,2,2,2]
     n = len(arr)

     sol = solution()
     sol.Frequency(arr, n)