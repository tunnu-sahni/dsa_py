#n meeting in one room

class solution:
    def maxMeetings(self, start, end):
        meetings = [(end[i], start[i]) for i in range(len(start))]
        meetings.sort()

        result = []
        last_end =-1

        for end_time, start_time in meetings:
            if start_time > last_end:
                result.append(start_time)
                last_end = end_time
                return len(result)
            
    
if __name__ == "__main__":
    start = [1, 3, 0, 5, 8, 5]
    end = [2, 4, 6, 7, 9, 9]

    sol = solution()
    res = sol.maxMeetings(start, end)
    print(res)


#jump game1

class JumpGame:
    def can_Jump(self, nums):
        max_index = 0

        for i in range(len(nums)):
            if i > max_index:
                return False
            max_index = max(max_index, i + nums[i])
        return True
    
if __name__ == "__main__":
    nums = [4, 3, 7, 1, 2]
    print("Array representing maximum jump from each index:", nums)
    game = JumpGame()
    ans = game.can_Jump(nums)
    if ans:
        print("can jump to the end of the array.")
    else:
        print("cannot jump to the end of the array.")