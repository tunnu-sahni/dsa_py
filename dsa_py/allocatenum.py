# allocate minimum number of pages

def countStudents(arr, pages):
    n = len(arr)
    students = 1
    pagesStudent = 0

    for i in range(n):
        if pagesStudent + arr[i] <= pages:
            pagesStudent += arr[i]

        else:
            students += 1
            pagesStudent = arr[i]

    return students

def findpages(arr, n, m):
    if m > n:
        return -1
    
    low = max(arr)
    high = sum(arr)

    for pages in range(low, high + 1):
        if countStudents(arr, pages) == m:
          return pages
        
    return low

arr = [25, 46, 28, 49, 24]
n = 5
m = 4
ans = findpages(arr, n, m)
print("the answer is:", ans)



#painters partion problem


from typing import List

class PainterPartition:
    def count_painters(self, boards: List[int], time: int) -> int:
        painters = 1
        boards_painter = 0

        for board in boards:
            if boards_painter + board <=  time:
                boards_painter += board

            else:
                painters += 1
                boards_painter = board

        return painters
    
    def find_largest_min_distance(self, boards: List[int], k: int) -> int:
        low = max(boards)
        high = sum(boards)

        for time in range(low, high + 1):
            if self.count_painters(boards, time) <= k:
                return time
        return low
    
boards = [10, 20, 30, 40]
k = 2

pp = PainterPartition()
ans = pp.find_largest_min_distance(boards, k)
print("the answer is:", ans)



from typing import List

class PainterPartation:
    def count_painters(self, boards: List[int], time: int) -> int:
        painters = 1
        boards_painter = 0

        for board in boards:

            if boards_painter + board <= time:
                boards_painter = board
        
        return painters
    
    def find_largest_min_distance(self, boards: List[int], k: int) -> int:
        low = max(boards)
        high = sum(boards)
        result = high 

        while low <= high:
            mid = (low + high ) // 2
            painters = self.count_painters(boards, min)

            if painters <= k:
                low = mid + 1

            else:
                result = mid
                high = mid - 1
        
        return result
    

boards = [1, 2, 3, 4, 5, 6]
k = 3

pp = PainterPartition()
ans = pp.find_largest_min_distance(boards, k)
print("the answer is:", ans)