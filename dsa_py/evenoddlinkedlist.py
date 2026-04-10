# #segregate even and odd nodes in linkedlist

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class solution:
#     def segregateEvenOdd(self, head):

#         if head is None or head.next is None:

#             return head
#         evenHead = evenTail = None
#         oddHead = oddTail = None
#         current = head

#         while current:

#             if current.data % 2 == 0:
#                 if not evenHead:
#                     evenHead = evenTail = current

#                 else:
#                     evenTail.next = current
#                     evenTail = current

#             else:
#                 if not oddHead:
#                     oddHead = oddTail = current

#                 else:
#                     oddTail.next = current
#                     oddTail = current

#             current = current.next

#         if not evenHead:
#             return oddHead
        
#         if not oddHead:
#             return evenHead
        
#         evenTail.next = oddHead
#         oddTail.next = None
#         return evenHead
#     def printList(head):
#         while head:
#             print(head.data, end=" ")
#             head = head.next

#     head = Node(17)
#     head.next = Node(15)
#     head.next.next = Node(8)
#     head.next.next.next = Node(12)
#     head.next.next.next.next = Node(10)

#     sol = solution()

#     newHead = sol.segregateEvenOdd(head)
#     printList(newHead)



#remove N-th node from the end of a linked list


# class Node:
#     def __init__(self, data1, next1=None):
#         self.data = data1
#         self.next = next1

# class solution:
#     def printList(self, head):
#         while head:
#             print(head.data, end=" ")
#             head = head.next

#     def deleteNthNodeFromEnd(self, head, N):

#         if head is None:
#             return None
#         cnt = 0
#         temp = head

#         while temp:
#             cnt += 1
#             temp = temp.next

#         if cnt == N:
#             return head.next
        
#         rec = cnt - N
#         temp = head

#         while temp:
#             res -= 1
#             if res == 0:
#                 break
#             temp = temp.next

#         temp.next = temp.next.next
#         return head
    
#     if __name__ == "__main__":
#         arr = [1, 2, 3, 4, 5]
#         N = 3

#         head = Node(arr[0])
#         head.next = Node(arr[1])
#         head.next.next = Node(arr[2])
#         head.next.next.next = Node(arr[3])
#         head.next.next.next.next = Node(arr[4])
#         head.next.next.next.next.next = Node(arr[5])

#         sol = solution()
#         head = sol.deleteNthNodeFromEnd(head, N)
        

        