#minimise maximum distance between gas stations

# class GasStationSolver:
#     def minimise_max_distance(self, arr, k):

#         n = len(arr)
#         how_many = [0] * (n - 1)

#         for _ in range(k):
#             max_section = -1
#             max_ind = -1

#             for i in range(n - 1):
#                 diff = arr[i + 1] - arr[i]
#                 section_length = diff / (how_many[i] + 1)

#                 if section_length > max_section:

#                     max_section = section_length
#                     max_ind = 1

#             how_many[max_ind] += 1

#         max_ans = -1
#         for i in range(n - 1):
#             deff = arr[i + 1] - arr[i]
#             section_length = diff / (how_many[i] + 1)
#             max_ans = max(max_ans, section_length)

#         return max_ans
    
# arr = [1, 2, 3, 4, 5]
# k = 4
# solver = GasStationSolver()
# ans = solver.minimise_max_distance(arr, k)
# print("the answer is", ans)



# import heapq

# class solution:
#     def minimiseMaxDistance(self, arr, k):
#         n = len(arr)
#         howMany = [0] * (n - 1)

#         pq = []
#         for i in range(n - 1):
#             dist = arr[i + 1] - arr[i]
#             heapq.heappush(pq, (-dist, i))

#         for _ in range(k):
#             negDist, idx = heapq.heapop(pq)
#             howMany[idx] += 1
#             totalDist = arr[idx + 1] - arr[idx]
#             newDist = totalDist / (howMany[idx] + 1)
#             heapq.heappush(pq, (-newDist, idx))

#         return -pq[0][0]
    
#     arr = [1, 2, 3, 4, 5]
#     k = 4

#     sol = solution()
#     print("the answer is", minimiseMaxDistance(arr, k))



# class GasStationOptimizer:
#     def number_of_gas_station_required(self, dist, arr):
#         count = 0

#         n = len(arr)

#         for i in range(1, n):
#             number_in_between = int((arr[i] - arr[i - 1]) / dist)

#             if (arr[i] - arr[i - 1]) == dist * number_in_between:
#                 number_in_between -= 1

#                 count += number_in_between 

#                 return count
            
#     def minimise_max_distance(self, arr, k):
#         low = 0
#         high = max(arr[i+1] - arr[i] for i in range(len(arr) - 1))

#         diff = 1e-6

#         while high - low > diff:
#             mid = (low + high) / 2.0
#             count = self.number_of_gas_station_required(mid, arr)

#             if count > k:
#                 low = mid

#             else:
#                 high = mid

#         return high
    
# if __name__ == "__main__":
#     arr = [1, 2, 3, 4, 5]
#     k = 4

#     optimizer = GasStationOptimizer()
#     result = optimizer.minimise_max_distance( arr, k)

#     print("the answer is:", result)




