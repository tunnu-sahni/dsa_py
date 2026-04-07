#check if the given linked list is palindrome

def b_search(elem, arr, n):
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == elem:
            return True
        
        elif arr[mid] < elem:
            start = mid + 1

        else:
            end = mid - 1
    
    return False

def is_subset(arr1, m, arr2, n):
    arr2.sort()

    if m > n:
        return False
    
    for i in range(m):
        present = b_search(arr1[i], arr2, n)

        if not present:
            return False
        
    return True

if __name__ == "__main__":

    arr1 = [1, 3, 4, 5, 2]
    arr2 = [2, 4, 3, 1, 7, 5, 15]

    m = len(arr1)
    n = len(arr2)

    ans = is_subset(arr1, m, arr2, n)

    if ans:
        print("arr1[] is a subset of arr2[]")

    else:
        print("arr1[] is not a subset of arr2[]")


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def reverse_linked_list(head):
    if head is None or head.next is None:
        return head
    
    new_head = reverse_linked_list(head.next)

    front = head.next

    front.next = head

    front.next = None

    return new_head

def is_palindrome(head):
    if head is None or head.next is None:
        return True
    
    slow = head
    fast = head

    while fast.next is not None and fast.next.next is not None:
        slow = slow.next

        fast = fast.next.next

        new_head = reverse_linked_list(slow.next)

        first = head
        second = new_head

        while second is not None:
            if first.data != second.data:
               reverse_linked_list

               return False
            
            first = first.next

            second = new_head

            while second is not None:

                if first.data != second.data:
                    reverse_linked_list(new_head)

                    return False
                first = first.next
                second = second.next

                reverse_linked_list(new_head)

                return True
            
    def print_linked_list(head):
        temp = head
        while temp:
            print(temp.data, end=" ")

            temp = temp.next

        print()

if __name__ == "__main__":

    head = Node(1)
    head.next = Node(5)
    head.next.next = Node(2)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(1)

    print("oroginal linked list:", end=" ")

    if is_palindrome(head):
        print("the linked list is a palindrome.")

    else:
        print("the linked list is not a palindrome.")