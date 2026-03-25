#find the highest/lowest frequency element

# class FrequencyCounter:
#     def countFreq(self, arr):
#         n = len(arr)

#         visited = [False] * n

#         maxFreq = 0
#         minFreq = n

#         maxEle = 0


#         for i in range(n):
#             if visited[i]:
#                 continue

#             count = 1

#             for j in range(i + 1, n):
#                 if arr[i] == arr[j]:
#                     visited[j] = True
#                     count += 1

#             if count < minFreq:
#                 minEle = arr[i]
#                 minFreq = count

#         print("the highest frequency element is:", maxEle)
#         print("the lowest frequency element is:", minEle)

# if __name__ == "__main__":
#     fc = FrequencyCounter()

#     arr = [10,5,10,15,10,5]
#     fc.countFreq(arr)


class FrequencyCounter:
    def Frequency(self, arr):
        freq_map = {}

        for num in arr:
            freq_map[num] = freq_map.get(num, 0) + 1
            maxFreq = 0
            minFreq = len(arr)
            maxEle = 0
            minEle = 0

            for element, count in freq_map.items():
                if count > maxFreq:
                    maxFreq = count
                    minEle = element

                    #print results
            print("the highest frequency element is:", maxEle)
            print("the lowest frequency element is:", minEle)

if __name__ == "__main__":
    fc = FrequencyCounter()
    arr = [10,5,10,15,10,5]
    fc.Frequency(arr)