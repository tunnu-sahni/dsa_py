# # sort k sorted array

# class solution:
#     def sortNearSortedArray(self, arr, k):
#         arr.sort()

#         return arr
    
# if __name__ == "__main__":
#     arr = [6, 5, 3, 2, 8, 10, 9]
#     k = 3
#     obj = solution()
#     result = obj.sortNearSortedArray(arr, k)

#     print(*result)


# import heapq
# from multiprocessing import heap

# class solution:
#     def sortNearlySortedArray(self, arr, k):
#         heap = []

#         result = []

#         for i in range(min(k + 1, len(arr))):
#             heapq.heappush(heap, arr[i])

#             for i in range(k + 1, len(arr)):
#                 result.append(heapq.heappop(heap))

#                 heapq.heappush(heap, arr[i])

#                 while heap:
                
#                     result.append(heapq.heappop(heap))
#                 return result
            
# if __name__ == "__main__":
#     arr = [6, 5, 3, 2, 8, 10, 9]
#     k = 3
#     obj = solution()
#     sorted_arr = obj.sortNearlySortedArray(arr, k)

#     print(*sorted_arr)


# #merge M sorted lists

# class ListNode:
#     def __int__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class solution:
#     def mergeSortedLists(self, lists):

#         all_values = []

#         for head in lists:
#             while head:
#                 all_values.append(head.val)
#                 head = head.next
#                 all_values.sort()

#                 dummy = ListNode(0)
#                 current = dummy

#                 for val in all_values:
#                     current.next = ListNode(val)
#                     current = current.next

#                 return dummy.next
            
# if __name__ == "__main__":
#     a = ListNode(1, ListNode(4, ListNode(5)))
#     b = ListNode(1, ListNode(3, ListNode(4)))
#     c = ListNode(2, ListNode(6))

#     lists = [a, b, c]

#     sol = solution()
#     result = sol.mergeSortedLists(lists)

#     while result:
#         print(result.val, end=" ")
#         result = result.next


#replace elements by its rank in the array


class solution:
    def replaceWithRank(self, arr):
        result = []

        for i in range(len(arr)):
            smaller = set()
            for j in range(len(arr)):
                if arr[j] < arr[i]:
                    smaller.add(arr[j])

            rank = len(smaller) + 1
            result.append(rank)

        return result
    
arr = [20, 15, 26, 2, 98, 6]
sol = solution()
print(sol.replaceWithRank(arr))


class solutiom:
    def replaceWithRank(self, arr):
        sorted_arr = sorted(set(arr))

        rank_map = {}
        rank = 1

        for num in sorted_arr:
            if num not in rank_map:
                rank_map[num] = rank
                rank += 1

        result = [rank_map[num] for num in arr]
        return result
    
obj = solution()
arr = [1, 5, 8, 15, 25, 9]
res = obj.replaceWithRank(arr)
print(res)


#task schedular

import heapq
from collections import Counter
from itertools import count
class solution:
    def leastInterval(self, tasks, n):
        freq = Counter(tasks)

        maxheap = [-count for count in freq.values()]
        heapq.heapify(maxheap)
        time = 0

        while maxheap:
            temp = []
            cycle = n + 1
            i = 0
            while i < cycle and maxheap:
               count = heapq.heappop(maxheap)
               count += 1
               if count < 0:
                     temp.append(count)
                     time += 1
                     i += 1

                     for item in temp:
                         heapq.heappush(maxheap, item)

                     if maxheap:
                         time += cycle - i
                         return time
                     
if __name__ == "__main__":
    sol = solution()
    tasks = ['A', 'A', 'A', 'B', 'B', 'B']
    n = 2
    print(sol.leastInterval(tasks, n))


#hand of straights


# from collections import counter
# import heapq

# class solution:
#     def isNStraightHand(self, hand, groupsSize):
#         if len(hand) % groupsSize != 0:
#             return False
        
#         freq = Counter(hand)
#         minheap = list(freq.keys())
#         heapq.heapify(minheap)

#         while minheap:
#             first = minheap[0]

#             for i in range(groupsSize):
#                 card = first + i

#                 if freq[card] == 0:
#                     return False
#                 freq[card] -= 1
#                 if freq[card] == 0 and card == minheap[0]:
#                     heapq.heappop(minheap)

#         return True
    
# if __name__ == "__main__":
#     sol = solution()

#     print(sol.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))

#     print(sol.isNStraightHand([1, 2, 3, 4, 5], 4))