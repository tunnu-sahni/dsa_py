#maximim rectangle area with all 1's 

class solution:
    def largestRectangleArea(self, heights):
        heights.append(0)

        stack = []
        max_area = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area,height * width)

        return max_area
    
    def maximalRectangle(self, matrix):
        if not matrix: return 0
        m = len(matrix[0])
        height = [0] * m
        max_area = 0

        for row in matrix:
            for i in range(m):
                if row[i] == '1':
                    height[i] += 1
                else:
                    height[i] = 0
            
            max_area = max(max_area, self.largestRectangleArea(height))

        return max_area
if __name__ == "__main__":
    matrix = [
        ['1', '0', '1', '0', '0'],
        ['1', '0', '1', '1', '1'],
        ['1', '1', '1', '1', '1'],
        ['1', '0', '0', '1', '0']
    ]
    sol = solution()

print(sol.maximalRectangle(matrix))