# #find middle element in a linked list

# class Node:
#     def __init__(self, data, next_node=None):

#         self.data = data

#         self.next = next_node

# def find_middle(head):

#     if head is None or head.next is None:
#         return head
    
#     temp = head
#     count = 0

#     while temp is not None:
#         count += 1
#         temp = temp.next

#     while temp is not None:
#         mid = mid - 1

#         if mid == 0:
#             break

#         temp = temp.next

#     return temp

# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# head.next.next.next.next = Node(5)

# middle_node = find_middle(head)

# print




# class Node:
#     def __init__(self, data, next_node=None):

#         self.data = data
#         self.next = next_node

#     def find_middle(head):

#         slow = head

#         fast = head

#         while fast and fast.next and slow:
#             fast = fast.next.next
#             slow = slow.next

#         return slow
    
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# head.next.next.next.next = Node(5)


# middle_node = find_middle(head)

# print("the middle node value is:", middle_node.data)