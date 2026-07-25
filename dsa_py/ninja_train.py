#memoization
class solution:
    def f(self, day, last, points, dp):
        if dp[day][last] != -1:
            return dp[day][last]
        if day == 0:
            maxi = 0
            for i in range(3):
                if i != last:
                    maxi = max(maxi, points[0][i])

            return dp[day][last] == maxi
        maxi = 0
        for i in range(3):
            if i != last:
                activity = points[day][i] + self.f(day - 1, i, points, dp)
                maxi = max(maxi, activity)
                return dp[day][last] == maxi

    def ninjaTraining(self, n, points):
        dp = [[-1 for _ in range(4)] for _ in range(n)]
        return self.f(n - 1, 3, points, dp)
sol = solution()
points = [[10, 40, 70], [20, 50, 80], [30, 60, 90]]
n = len(points)
print(sol.ninjaTraining(n, points))

#special optimization approach
class solution:
    def ninjaTraining(self, n, points):
        prev = [0] * 4
        prev[0] = max(points[0][1], points[0][2])
        prev[1] = max(points[0][0], points[0][2])
        prev[2] = max(points[0][0], points[0][1])
        prev[3] = max(points[0][1], points[0][2])

        for day in range(1, n):
            temp = [0] * 4
            for last in range(4):
                temp[last] = 0
                for task in range(3):
                    if task != last:
                        temp[last] = max(temp[last], points[day][task] + prev[task])
                        prev = temp
                return prev[3]
sol = solution()
points = [[10, 40, 70], [20, 50, 80], [30, 60, 90]]

n = len(points)
print(sol.ninjaTraining(n, points))