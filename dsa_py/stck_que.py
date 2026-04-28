# # implement queue using stack

# class ArrayQueue:
#     def __init__(self):
#         self.arr = [0] * 10

#         self.start = -1
#         self.end = -1

#         self.currSize = 0
#         self.maxSize = 10

#     def push(self, x):
#         if self.currSize == self.maxSize:
#             print("Queue is full\nExisting...")
#             exit(1)

#         if self.end == -1:
#             self.start = 0
#             self.end = 0

#         else:
#             self.end = (self.end + 1) % self.maxSize
#             self.arr[self.end] = x
#             self.currSize += 1
#     def pop(self):
#         if self.start == -1:
#             print("Queue is empty\nExiting...")
#             exit(1)

#         popped = self.arr[self.start]

#         if self.currSize == 1:
#             self.start = -1
#             self.end = -1
        
#         else:
#             self.start = (self.start + 1) % self.maxSize
#             self.currSize -= 1
#             return popped
        
#     def peek(self):
#         if self.start == -1:
#             print("Queue is empty")
#             exit(1)

#         return self.arr[self.start]
#     def isEmpty(self):
#         return self.currSize == 0
    
# if __name__ == "__main__":
#     queue = ArrayQueue()
#     commands = ["ArrayQueue", "push", "push", "peek", "pop", "pop", "isEmpty"]
#     inputs = [[], [5], [10], [], [], [], []]

#     for i in range(len(commands)):
#         if commands[i] == "push":
#             queue.push(inputs[i][0])
#             print("null", end=" ")

#         elif commands[i] == "pop":
#             print(queue.pop(), end=" ")

# #implement queue using stack

# class StackQueue:
#     def __init__(self):
#         self.st1 = []
#         self.st2 = []

#     def push(self, x):
#         while self.st1:
#             self.st2.append(self.st1.pop())
#         self.st1.append(x)

#         while self.st2:
#             self.st1.append(self.st2.pop())

#     def pop(self):
#         if not self.st1:
#             print("Stack is empty")
#             return -1
        
#         top_element = self.st1.pop()
#         return top_element
    
#     def peek(self):
#         if not self.st1:
#             print("Stack is empty")
#             return -1
        
#         return self.st1[-1]
    
#     def is_empty(self):
#         return not self.st1
# if __name__ == "__main__":
#     q = StackQueue()
#     commands = ["StackQueue", "push", "push", "pop", "peek", "isEmpty"]
#     inputs = [[], [4], [8], [], [], []]

#     for i in range(len(commands)):
#         if commands[i] == "push":
#             q.push(inputs[i][0])

#             print("null", end=" ")

#         elif commands[i] == "pop":
#             print(q.pop(), end=" ")

#         elif commands[i] == "peek":
#             print(q.peek(), end=" ")

#         elif commands[i] == "isEmpty":
#             print("true" if q.is_empty() else "false", end=" ")
        
#         elif commands[i] == "StackQueue":
#             print("null", end=" ")

# using two stacks where push operations is O(1)

# class StackQueue:
#     def __init__(self):
#         self.input = []
#         self.output = []

#     def push(self, x: int):
#         self.input.append(x)

#     def pop(self) -> int:
#         if not self.output:
#             while self.input:
#                 self.output.append(self.input.pop())

#         if not self.output:
#             print("Queue is empty, cannot pop.")
#             return -1
        
#         return self.output.pop()
    
#     def peek(self) -> int:
#         if not self.output:
#             while self.input:
#                 self.output.append(self.input.pop())

#         if not self.output:
#             print("Queue is empty, cannot peek.")
#             return -1
        
#         return self.output[-1]
    
#     def isEmpty(self) -> bool:
#         return not self.input and not self.output
    
# if __name__ == "__main__":
#     q = StackQueue()
#     q.push(3)
#     q.push(4)
#     print("The element popped is", q.pop())

#     q.push(5)
# #     print("The front of the queue is", q.peek())

# #     print("Is the queue empty?", "yes" if q.isEmpty() else "No")
# #     print("The element popped is", q.pop())

# #     print("The element popped is", q.pop())

# #     print("Is the queue empty?", "yes" if q.isEmpty() else "no")


# # implement stack using linked list

# class Node:
#     def __init__(self):
#         self.val = None
#         self.next = None

# class LInkedListStack:
#     def __init__(self):
#         self.head = None
#         self.size = 0

#     def push(self, x):
#         element = Node(x)

#         element.next = self.head
#         self.head = element
#         self.size += 1

#     def pop(self):
#         if self.head is None:
#             return -1
        
#         value = self.head.val
#         temp = self.head
#         self.head = self.head.next
#         del temp 
#         self.size -= 1

#         return value
#     def top(self):
#         if self.head is None:
#             return -1
        
#     def isEmpty(self):
#         return self.size == 0
# st = LInkedListStack()

# commands = ["LinkedListStack", "push", "push", "pop", "top", "isEmpty"]
# #list of input
# inputs = [[], [3], [7], [], [], []]

# for i in range(len(commands)):
#     if commands[i] == "push":
#         st.push(inputs[i][0])
#         print("null", end=" ")

#     elif commands[i] == "pop":
#         print(st.pop(), end=" ")

#     elif commands[i] == "top":
#         print(st.top(), end=" ")

#     elif commands[i] == "isEmpty":
#         print("true" if  st.is_empty() else "false", end=" ")

#     elif commands[i] == "LinkedlistStack":
#         print("null", end=" ")

class solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            
            else:
                if not stack:
                    return False
                top = stack.pop()

                if (ch ==')' and top == '(') or \
                   (ch == ']' and top == '[') or \
                   (ch == '}' and top == "{"):
                    continue
                else:
                    return False
            
        return not stack

sol = solution()
s = "()[{}()]"
if sol.isValid(s):
    print("True")
else:
    print("False")