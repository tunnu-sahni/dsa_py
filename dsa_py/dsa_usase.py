#bfs(breath first search)

# from collections import deque

# def bfs(graph, start):
#     visited = set()
#     q = deque([start])

#     visited.add(start)

#     while q:
#         node = q.pop()
#         print(node, end=" ")

#         for neighbor in graph[node]:
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 q.append(neighbor)

# #graph
# graph = {
#     1: [2, 3],
#     2: [4],
#     3: [5],
#     4: [],
#     5: []
# }

# bfs(graph, 1)



# from collections import deque

# def bfs(graph, start):
#     visited = set()
#     q = deque([start])

#     visited.add(start)

#     while q:
#         node = q.pop()
#         print(node, end=" ")

#         for neighbor in graph[node]:
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 q.append(neighbor)

# graph = {
#     1: [2, 3],
#     2: [4],
#     3: [5],
#     4: [],
#     5: []
# }

# bfs(graph, 1)


#level order traversal


# from collections import deque

# class node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

# def level_order(root):
#     if not root:
#         return
    
#     q = deque([root])

#     while q:
#         node = q.pop()
#         print(node.val, end=" ")

#         if node.left:
#             q.append(node.right)



#tree create

# root = node(1)
# root.left = node(2)
# root.right = node(3)
# root.left.left = node(4)
# root.left.right = node(5)

# level_order(root)


#sliding window problem

from collections import deque

def max_sliding_window(nums, k):
    q = deque()
    result = []

    for i in range(len(nums)):
        #remove out of window
        if q and q[0] == i - k:
            q.pop()

            #remove smaller elements

        while q and nums[q[-1]] < nums[i]:
            q.pop()

        q.append(i)

        if i >= k - 1:
            result.append(nums[q[0]])

    return result

nums = [1,3, -1, -3, 5,3,6,7]
print(max_sliding_window(nums, 3))


#scheduling task queue


from collections import deque

tasks = deque(["Task1", "Task2", "Task3"])

while tasks:
    current = tasks.pop()
    print("processing:", current)