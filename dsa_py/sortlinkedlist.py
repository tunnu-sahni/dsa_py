# #sort a linked list

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# def merge(l1, l2):
#     dummy = Node(0)
#     tail = dummy

#     while l1 and l2:
#         if l1.data < l2.data:
#             tail.next = l1
#             l1 = l1.next

#         else:
#             tail.next = l2
#             l2 = l2.next

#         tail = tail.next
#     tail.next = l1 if l1 else l2
#     return dummy.next

# def get_middle(head):
#     slow = head
#     fast = head.next

#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next


#     return slow

# def sort_list(head):
#     if not head or not head.next:
#         return head
#     mid = get_middle(head)
#     right = mid.next
#     mid.next = None

#     left = sort_list(head)
#     right = sort_list(right)

#     return merge(left, right)



