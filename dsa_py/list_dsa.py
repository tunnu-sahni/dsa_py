# arr = [10,20,30]

# print(arr)

# #list create

# arr = [1,2,3]
# arr2 = list((4,5,6))
# print(arr+arr2)

# arr1 = [10,20,30,40]
# arr2 = [50,60,70,80]

# print(arr1+arr2)



#access elements

# arr = [10,20,30]

# print(arr[0])
# print(arr[-1])

# #insert functions

# arr = [1,2,3,4,5,6]

# arr.append(7)
# print(arr)


# list = [10,20,30,40,50,60,70]
# list.append(80)
# print(list)


# list = [1,2,3,4,5]
# list.insert(1, 100)
# print(list)

# #extend(multiple elements add)

# list = [1,2,3,4,5,6]
# list.extend([7, 8])
# print(list)

# arr = [10,20,30,405,5,66]
# arr.extend([34, 55,68])
# print(arr)


#delete functions

# arr = [1,2,3,4,5]
# arr.pop(2)
# print(arr)


# list = [10,20,30,40,50,60,70]
# list.remove(30)
# print(list)
# list.remove(70)
# print(list)


# arr = [1,2,3,4,5,6]
# arr.clear()
# print(arr)


# list = [1,2,3,4,5]
# del list[0]
# print(list)


# arr = [10,203,44,59,88]
# del arr[3]
# print(arr)


# #search functions

# arr = [1,2,3,4,5,6]
# if 4 in arr:
#     print("Found")


# list = [1,2,3,4]
# print(list.index(4))
# print(list.index(2))


# arr = [10,20,30,40,50]
# print(arr.count(20))


# list = [1,2,3,4,5,6,7]
# print(list.count(4))


# #traversal


# arr = [1,2,3,4,5]
# for x in arr:
#     print(x)

# list = [10,20,30,40,50]
# for x in list:
#     print(x)


#reverse & sort

# arr = [1,2,3,4,5]
# arr.reverse()
# print(arr)


# list = [10,20,30,40,50]
# list.reverse()
# print(list)


# list = [1,2,3,4,5]
# list.sort()
# print(list)

# s = [10,20,30,40,50]
# s.sort()
# print(s)


# arr = [1,2,3]
# new_arr = sorted(arr)
# print(arr)

# arr = [1,2,3,4,5]
# print(len(arr))

# list = [10,20,30,40]
# print(len(arr))


# list = [1,2,3,4]
# if not arr:
#     print("Empty")


# #slicing

# arr = [1,2,3,4,5]

# print(arr[1:4])
# print(arr[:3])
# print(arr[::-1])


# list = [1,2,3,4,5,6,7]

# print(arr[3:])
# print(arr[::])
# print(arr[2:4])


arr = [1,2,3,4]
new_arr = arr.copy()
print(arr)


list = [10,20,30,40,50]
new_list = list.copy()
print(list)


#nested list

arr = [[1,2], [3,4]]
print(arr[0][1])  