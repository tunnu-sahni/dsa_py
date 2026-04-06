#reverse a linked list

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class solution:
#     def reverseList(self, head):
#         stack = []
#         temp = head

#         while temp:
#             stack.append(temp.val)
#             temp = temp.next

#         temp = head

#         while temp:
#             temp.val = stack.pop()
#             temp = temp.next

#             return head
# def printList(head):
#     while head:
#         print(head.val, end=" ")
#         head = head.next

# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)

# sol = solution()
# head = sol.reverseList(head)
# printList(head)


# class ListNode:
#     def __init__(self, val=0):

#         self.val = val
#         self.next = None

# class solution:
#     def reverseList(self, head):

#         prev = None
#         temp = head

#         while temp:
#             front = temp.next
#             temp.next = prev
#             prev = temp
#             temp = front
#         return prev
    
# def printList(head):
#     while head:
#         print(head.val, end=" ")
#         head = head.next

#     print()

# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)

# sol = solution()

# newHead= sol.reverseList(head)

# printList(newHead)



# class ListNode:
#     def __init__(self, val=0):
#         self.val = val
#         self.next = None

# class sulution:
#     def reverseList(self, head):
#         if head is None or head.next is None:
#             return head
        
#         newHead = self.reverseList(head.next)

#         front = head.next

#         front.next = head
#         head.next = None

#         return newHead
    
# if __name__ == "__main__":

#     head = ListNode(1)
#     head.next = ListNode(2)
#     head.next.next = ListNode(3)
#     head.next.next.next = ListNode(4)
#     head.next.next.next.next = ListNode(5)

#     sol = solution()
#     reversed_head = sol.reverseList(head)

#     while reversed_head:
#         print(reversed_head.val, end=" ")

#         reversed_head = reversed_head.next


# #detect a cycle in a linked list

# class Node:
#     def __init__(self, data1, next1=None):
#         self.data = data1
#         self.next = next

# class solution:
#     def detectLoop(self, head):

#         temp = head
#         nodeMap = {}

#         while temp is not None:
#             if temp in nodeMap:
#                 return True
            
#             nodeMap[temp] = 1

#             temp = temp.next

#         return False
    
# if __name__ == "__main__":

#     head = Node(1)
#     second = Node(2)
#     third = Node(3)
#     fourth = Node(4)
#     fifth = Node(5)

#     head.next = second
#     second.next = third
#     third.next = fourth
#     fourth.next = fifth
#     fifth.next = third

#     sol = solution()

#     if sol.detectLoop(head):
#         print("loop detected in the linked list.")

#     else:
#         print("no loop detected in the linked list.")


#starting point of loop in a linked

# class ListNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

# class solution:
#     def detectCycle(self, head):

#         visited = set()

#         while head:
#             if head in visited:
#                 return head
            
#             visited.add(head)

#             head = head.next

#         return None
    
# if __name__ == "__main__":
#     head = ListNode(3)
#     head.next = ListNode(2)
#     head.next.next = ListNode(0)
#     head.next.next.next = ListNode(-4)

#     head.next.next.next.next = head.next
#     obj = solution()
#     startnode = obj.detectCycle(head)

#     if startNode:
#         print("Cycle starts at node with value:", startNode.val)
#     else:
#         print("no cycle found.")


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class solution:
    def detectCycle(self, head):

        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next

            if slow == fast:
                slow = head

                while slow!= fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
    
if __name__ == "__main__":

    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next

    obj = solution()
    result = obj.detectCycle(head)

    if result:
        print("Cycle starts at node with value:", result.val)

    else:
        print("no cycle found.")