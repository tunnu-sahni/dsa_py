# course schedue 1 and 2

from collections import deque

class solution:
    def canFinish(self, numcourses, preprequisites):
        adj = [[] for _ in range(numcourses)]
        indegree = [0] * numcourses

        for a, b in preprequisites:
            adj[b].append(a)
            indegree[a] += 1

        q = deque([i for i in range(numcourses)])
        
        count = 0

        while q:
            node = q.popleft()
            count += 1

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return count == numcourses
    
if __name__ == "__main__":
    sol = solution()
    preprequisites = [[1, 0], [0, 1]] 
    numcourses = 2
    print(sol.canFinish(numcourses, preprequisites))

#time complexity O(v+e)
#space complexity O(v+e)


# schedule 2

from collections import deque

class solution:
    def findOrder(self, numcourses, prerequisites):
        adj = [[] for _ in range(numcourses)]

        indegree = [0] * numcourses

        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1

        q = deque([i for i in range(numcourses)])
        
        order = []
        while q:
            node = q.popleft()
            order.append(node)

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

            return order if len(order) == numcourses else []

if __name__ == "__main__":
    sol = solution()
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]

    numcourses = 4
    print(sol.findOrder(numcourses, prerequisites))

