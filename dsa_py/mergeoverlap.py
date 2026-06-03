# merge overlapping sub intervals

from typing import List
class solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        ans = []
        n = len(intervals)
        i = 0

        while i < n:
            start = intervals[i][0]
            end = intervals[i][1]

            j = i + 1
            while j < n and intervals[j][0] <= end:
                j += 1
                ans.append([start, end])
                i = j
        return ans
            
sol = solution()
intervals = [[1, 3], [2, 6],[8, 10], [15, 18]]
print("Merged intervals:", sol.merge(intervals))


from typing import List

class Solution:
    # Function to merge overlapping intervals
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals based on the start time
        intervals.sort()

        # List to store final merged intervals
        merged = []

        # Traverse all intervals
        for interval in intervals:
            # If merged list is empty or current interval doesn't overlap
            if not merged or merged[-1][1] < interval[0]:
                # Append current interval as a new one
                merged.append(interval)
            else:
                # Overlapping: merge by extending the end
                merged[-1][1] = max(
                    merged[-1][1],
                    interval[1]
                )

        return merged

# Example usage
sol = Solution()
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(sol.merge(intervals))


# non overlapping

class Solution:
    # Function to find the minimum number of intervals to remove to make all intervals non-overlapping
    def eraseOverlapIntervals(self, intervals):
        
        # Total number of intervals
        n = len(intervals)
        
        # Track max valid non-overlapping subset
        max_valid = 0

        # Try all subsets using bitmasking
        for mask in range(1 << n):

            # Build current subset
            subset = []
            for i in range(n):
                if mask & (1 << i):
                    subset.append(intervals[i])

            # Sort the subset
            subset.sort()

            # Check if it is non-overlapping
            valid = True
            for i in range(1, len(subset)):
                if subset[i][0] < subset[i - 1][1]:
                    valid = False
                    break

            # Update max valid
            if valid:
                max_valid = max(max_valid, len(subset))

        # Return total - max valid
        return n - max_valid

# Driver code
if __name__ == "__main__":
    sol = Solution()
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print("Minimum intervals to remove:", sol.eraseOverlapIntervals(intervals))