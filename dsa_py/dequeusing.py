#implement deque using python

# from collections import deque
# dq = ([1,2,3,4,56])

# dq = deque()
# #insert

# dq.append(10)
# dq.appendleft(5)
# #delete

# dq.pop()
# dq.popleft()

# print(dq)

#check palindrome

# from collections import deque

# def is_palindrome(s):
#     dq = deque(s)

#     while len(dq) > 1:
#         if dq.popleft() !=dq.pop():
#             return False
#     return True

# print(is_palindrome("racecar")) 


# arr = [1,3,-1,-3,5,3,6,7]
# k = 3


# from collections import deque

# def max_sliding_window(nums, k):
#     dq = deque()
#     result = []

#     for i in range(len(nums)):

#         if dq and dq[0] ==i - k:
#             dq.popleft()

#         while dq and nums[dq[-1]] < nums[i]:
#             dq.pop()

#             dq.append(i)

#             if i >= k - 1:
#                 result.append(nums[dq[0]])

#     return result

# print(max_sliding_window([1,3,-1,-3,5,3,6,7], 3))


from collections import deque

class LRUcache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dq = deque()
        self.map = {}

    def get(self, key):
        if key not in self.map:
            return -1
        
    def put(self, key, value):
        if key in self.map:
            self.dq.remove(key)

        elif len(self.dq) == self.capacity:
            oldest = self.dq.popleft()
            del self.map[oldest]

        self.dq.append(key)
        self.map[key] = value

