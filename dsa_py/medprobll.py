#length of loo in linked list

class Node:
    def __init__(self, data1, next1=None):

        self.data = data1
        self.next = next1

class solution:
    def lengthOfLoop(self, head):
        visitednodes = {}

        temp = head
        timer = 0

        while temp is not None:
            if temp in visitednodes:
                loopLength = timer - visitednodes[temp]

                return loopLength
            visitednodes[temp] = timer

            temp = temp.next
            timer += 1

            return 0
        
if __name__ == "__main__":
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = second

    obj = solution()

    loopLength = obj.lengthOfLoop(head)

    if loopLength > 0:
        print("length of the loop:", loopLength)
    
    else:
        print("no loop found in the linked list.")
        


class Node:
    def __init__(self, data1, next1=None):

        self.data = data1
        self.next = next

class solution:
    def lengthOfLoop(self, head):

        slow = head
        fast = head

        while fast is not None and fast.next is not None:

            slow = slow.next

            fast = fast.next.next

            if slow == fast:
                return self.countLoopLength(slow)
        return 0
    
    def countLoopLength(self, meetingPoint):
        temp = meetingPoint
        length = 1

        while temp.next != meetingPoint:
            temp = temp.next
            length += 1
        return length
    
if __name__ == "__main__":
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourht = Node(4)
    fifth = Node(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = second

    obj = solution()

    loopLength = obj.lengthOfLoop(head)

    if loopLength > 0:
        print("Length of the loop:", loopLength)

    else:
        print("No loop found the linked list.")

