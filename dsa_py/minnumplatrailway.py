# minimum number of platform rquired for a railway

class solution:
    def countplatforms(self, n, arr, dep):
        ans = 1
        for i in range(n):
            count = 1
            for j in range(i + 1, n):
                if (arr[i] >= arr[j] and arr[i] <= dep[j]) or \
                     (arr[j] >= arr[i] and arr[j] <= dep[i]):
                    count += 1
                    ans = max(ans, count)
        return ans
    
arr = [900, 945, 955, 1100, 1500, 1800]
dep = [920, 1200, 1130, 1150, 1900, 2000]
n = len(arr)

sol = solution()
print("Minimum platforms required:", sol.countplatforms(n, arr, dep))


class solution:
    def countPlatforms(self, arr, dep, n):
        arr.sort()
        dep.sort()

        platforms = 1
        result = 1
        i, j = 1, 0

        while i < n and j < n:
            if arr[i] <= dep[j]:
                platforms += 1
                i += 1
            else:
                platforms -= 1
                j += 1
                result = max(result, platforms)
        return result
    
arr = [900, 945, 955, 1100, 1500, 1800]
dep = [920, 1200, 1130, 1150, 1900, 2000]
n = len(arr)

sol = solution()
print("Minimum number of platforms required", sol.countPlatforms(arr, dep, n))

# job sequencing problem

class job:
    def __init__(self, id, dead, profit):
        self.id = id
        self.dead = dead
        self.profit = profit

    def jobsequencing(arr, n):
        arr.sort(key=lambda x: x.profit, reverse=True)
        maxi = arr[0].dead
        for i in range(1, n):
            maxi = max(maxi, arr[i].dead)

        slot = [-1] * (maxi + 1)

        countjobs = 0
        jobprofit = 0

        for i in range(n):
            for j in range(arr[i].dead, 0, -1):
                if slot[j] == -1:
                    slot[j] = i
                    countjobs += 1
                    jobprofit += arr[i].profit
                    break

        return countjobs, jobprofit
    
if __name__ == "__main__":
    n = 4
    arr =[job(1, 4, 20), job(2, 1, 10), job(3, 2, 40), job(4, 2, 30)]

    ans = job.jobsequencing(arr, n)
    print("Number of jobs done:", ans[0])
    print("Total profit:", ans[1])