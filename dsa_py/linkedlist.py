#insert at the head of a linked list (new node ko list ke starting me add karna)

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# def insert_at_head(head, val):
#     new_node = Node(val)
#     new_node.next = head
#     return new_node

# def print_list(head):
#     temp = head
#     while temp:
#         print(temp.data, end=" ->")
#         temp = temp.next

#     print_list(head)


#introduction to doubly linked list


# class Node:
#     def __init__(self, data, next=None):

#         self.data = data
#         self.next = next

# if __name__ == "__main__":
#     arr = [2, 5, 8, 7]

#     y = Node(arr[0])
#     y = Node(arr[2])
#     y = Node(arr[3])

#     print(y)

#     print(y.data)


# #doubly llinked list


# class Node:
#     def __init__(self, data, next=None, prev=None):

#         self.data = data
#         self.next = next
#         self.prev = prev

# arr = [2, 5, 8, 7]

# head = Node(arr[0])

# print(head)

# print(head.data)

# #insert at end of doubly linked list(new node ko last me add karna)

# class Node:
#     def __init__(self, data, next_node=None, back_node=None):

#         self.data = data
#         self.next = next_node
#         self.back = back_node

# def convertArr2DLL(arr):
#     head = Node(arr[0])

#     prev = head

#     for i in range(1, len(arr)):
#         temp = Node(arr[i], None, prev)

#         prev.next = temp
#         prev = temp

#     return head

# def printList(head):
#     while head:
#         print(head.data, end=" ")

#     print()

# def insertAtTail(head, k):
#     newNode = Node(k)

#     if not head:
#         return newNode
    
#     tail = head
#     while tail.next:
#         tail = tail.next

#     tail.next = newNode
#     newNode.back = tail

#     return head

# if __name__ == "__main__":
#     arr = [12, 5, 8, 7, 4]
#  head = convertArr2DLL(arr)

    
#     print("doubly linked list initialy:")
#     printList(head)


#     print("\ndoubly linked list after inserting at the tail with value 10:")

#     head = insertAtTail(head, 10)
#     printList(head)


#delete last node of a doubly linked list

# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.prev = None
#         self.next = None

# class solution:
#     def deleteTail(self, head):
#         if not head:
#             return None
        
#         if not head.next:
#             return None
        
#         temp = head
#         while temp.next:
#             temp = temp.next

#             temp.prev.next = None
#             return head
        
# if __name__ == "__main__":

#     head = Node(1)
#     head.next = Node(2)
#     head.next.prev = head
#     head.next.next = Node(3)
#     head.next.next.prev = head.next

#     obj = solution()
#     head = obj.deleteTail(head)
#     curr = head
#     while curr:
#         print(curr.data, end="")
#         curr = curr.next


# #reverse a doubly linked list

# class Node:
#     def __init__(self, data, next=None, back=None):
#         self.data = data
#         self.next = next
#         self.back = back

# def convertArr2DLL(arr):
#     head = Node(arr[0])

#     prev = head

#     for i in range(1, len(arr)):

#         temp = Node(arr[i], None, prev)
#         prev.next = temp
#         prec = temp

#     return head

# def printDLL(head):

#     while head:
#         print(head.data, end=" ")
#         head = head.next


# def reverseDLL(head):
#     if not head or not head.next:
#         return head
#     stack = []

#     temp = head

#     while temp:
#         stack.append(temp.data)
#         temp = temp.next

#     temp = head

#     while temp:
#         temp.data = stack.pop()
#         temp = temp.next

#     return head

# arr = [12, 5, 8, 7, 4]
# head = convertArr2DLL(arr)
# print("doubly linked list initially:")
# printDLL(head)
# head = reverseDLL(head)

# print("\doubly linked list after reverseing:")
# printDLL(head)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def convert_list_to_dll(arr):
    head = Node(arr[0])

    prev = head
    for i in range(1, len(arr)):

        new_node = Node(arr[i])
        new_node.prev = prev

        prev.next = new_node

        prev = new_node
    
    return head

def reverse_dll(head):
    temp = None
    current = head

    while current is not None:

        temp = current.prev
        current.prev = current.next
        current.next = temp

        current = current.prev

        if temp is not None:
            head = temp.prev

        return head
    
def print_dll(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    head = convert_list_to_dll(arr)

    print("original DLL:")

    print_dll(head)

    head = reverse_dll(head)

    print("reversed DLL:")

    print_dll(head)
