class DisjointSet:
    # To store the ranks, parents and 
    # sizes of different set of vertices
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)
    
    # Function to find ultimate parent
    def findUPar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]
    
    # Function to implement union by rank
    def unionByRank(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1
    
    # Function to implement union by size
    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]
    
    def getSize(self, node):
        return self.size[self.findUPar(node)]

# Solution class
class Solution:
    # DelRow and delCol for neighbors
    delRow = [-1, 0, 1, 0]
    delCol = [0, 1, 0, -1]
    
    # Helper function to check if a 
    # pixel is within boundaries
    def isValid(self, i, j, n):
        # Return false if pixel is invalid
        if i < 0 or i >= n:
            return False
        if j < 0 or j >= n:
            return False
        # Return true if pixel is valid
        return True
    
    # Function to add initial islands to the 
    # disjoint set data structure
    def addInitialIslands(self, grid, ds, n):
        # Traverse all the cells in the grid
        for row in range(n):
            for col in range(n):
                # If the cell is not land, skip
                if grid[row][col] == 0:
                    continue
                
                # Traverse on all the neighbors
                for ind in range(4):
                    # Get the coordinates of neighbor
                    newRow = row + self.delRow[ind]
                    newCol = col + self.delCol[ind]
                    
                    # If the cell is valid and a land cell
                    if (self.isValid(newRow, newCol, n) and 
                        grid[newRow][newCol] == 1):
                            
                        # Get the number for node
                        nodeNo = row * n + col
                        # Get the number for neighbor
                        adjNodeNo = newRow * n + newCol
                        
                        # Take union of both nodes as 
                        # they are part of the same island
                        ds.unionBySize(nodeNo, adjNodeNo)
    
    # Function to get the size of the largest island
    def largestIsland(self, grid):
        # Dimensions of grid
        n = len(grid)
        
        # Disjoint set data structure
        ds = DisjointSet(n * n)
        
        # Function call to add initial 
        # islands in the disjoint set
        self.addInitialIslands(grid, ds, n)
        
        # To store the answer
        ans = 0
        
        # Traverse on the grid
        for row in range(n):
            for col in range(n):
                # If the cell is a land cell, skip
                if grid[row][col] == 1:
                    continue
                
                # Set to store the ultimate 
                # parents of neighboring islands
                components = set()
                
                # Traverse on all its neighbors
                for ind in range(4):
                    # Coordinates of neighboring cell
                    newRow = row + self.delRow[ind]
                    newCol = col + self.delCol[ind]
                    
                    if (self.isValid(newRow, newCol, n) and 
                        grid[newRow][newCol] == 1):
                        # Perform union and store 
                        # ultimate parent in the set
                        nodeNumber = newRow * n + newCol
                        components.add(ds.findUPar(nodeNumber))
                
                # To store the size of current largest island
                sizeTotal = 0
                
                # Iterate on all the neighboring ultimate parents
                for parent in components:
                    # Update the size
                    sizeTotal += ds.getSize(parent)
                
                # Store the maximum size of island
                ans = max(ans, sizeTotal + 1)
        
        # Edge case
        for cellNo in range(n * n):
            # Keep the answer updated
            ans = max(ans, ds.getSize(cellNo))
        
        # Return the answer
        return ans

# Main function to test the Solution class
if __name__ == "__main__":
    grid = [
        [1, 0],
        [0, 1]
    ]

    # Creating instance of Solution class
    sol = Solution()
    
    # Function call to get the size of the largest island
    ans = sol.largestIsland(grid)
    
    # Output
    print("The size of the largest island is:", ans)