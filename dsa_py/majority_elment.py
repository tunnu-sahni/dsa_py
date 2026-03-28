#majority element

         
# def majorityElement(nums):
#     count = 0
#     candidate = None

#     for num in nums:
#         if count == 0:
#             candidate = num
        
#         count += (1 if num == candidate else -1)

#     return [candidate]   # return list so loop chale

# ans = majorityElement([2,2,1,1,2])
# for i in ans:
#     print(i)



from collections import defaultdict
from typing import List

class solution:
    def majorityElementTwo(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []

        mpp = defaultdict(int)
        mini = n // 3 + 1

        for num in nums:
            mpp[num] += 1

            if mpp[num] == mini:
                result.append(num)

            if len(result) == 2:
                break
        return result
    
if __name__ == "__main":
    arr = [11, 33, 33, 11, 33, 11]
    sol = solution()
    ans = sol.majorityElementTwo(arr)

    print("the majority element are:", *ans)