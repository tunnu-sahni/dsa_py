#capacity to ship packages within D days

class solution:
    def daysNeeded(self, wieghts, capacity):

        days = 1

        currentLoad = 0

        for w in wieghts:
            if currentLoad + w > capacity:
                days += 1
                currentLoad = w

            else:

                currentLoad += w

        return days
    def shipWithinDays(self, wieghts, d):

        left = sum(wieghts)

        right = max(weights)

        for capacity in range(left, right + 1):

            needed = self.daysNeeded(weights, capacity)

            if needed <= d:
                return right 
            
if __name__ == "__main__":
    weights = [5,4,5,2,3,4,5,6]

    d = 5
    sol = solution()
    print(sol.shipWithinDays(weights, d))



class solution:
    def daysNeeded(self, weights, capacity):
        days = 1
        currentLoad = 0

        for w in weights:
            if currentLoad + w > capacity:
                days += 1
                currentLoad = w

            else:
                currentLoad += w

        return days
    
    def shipWithinDays(self, weights, d):
        left = max(weights)

        right = sum(weights)

        while left < right:
            mid = left + (right - left) // 2
            needed = self.daysNeeded(weights, mid)

            if needed <= d:
                right = mid
            else:
                left = mid + 1

        return left
    
if __name__ == "__main__":
    weights = [5,4,5,2,3,4,5,6]

    d = 5
    sol = solution()
    print(sol.shipWithinDays(weights, d))
