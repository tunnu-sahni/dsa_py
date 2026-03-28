#program to generate pascal triangle

# def pascal_triangle(n):
#     triangle = []

#     for i in range(n):
#         row = [1] * (i + 1)

#         for j in range(1, i):
#             row[j] = triangle[i-1][j-1] + triangle[i-1][j]

#             triangle[i-1][j]

#             triangle.append(row)

#             return triangle
        
# n = int(input("enter number of rows: "))
# result = pascal_triangle(n)

# for row in result:
#     print(row)



def pascal_triangle(n):
    for i in range(n):
        num = 1
        for j in range(i + 1):
            print(num, end=" ")
            num = num * (i - j) // (j + 1)
        
        print()

n = int(input("enter rows: "))
pascal_triangle(n)