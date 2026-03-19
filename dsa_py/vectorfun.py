# arr = [10, 20, 30]

# print(arr[0])
# print(arr[-1])
# print(arr[1:3])
# print(arr[1])

# arr = [1,2,3,4]
# print(arr[2])

# # rbegin/rend

# arr = [1,2,3,4]

# for x in reversed(arr):
#     print(x)


# arr = [10,20,30,40,50]

# for x in reversed(arr):
#     print(x)


# #cbegin/cend

arr = [1,2,3]
for x in arr:
    print(x)

#push back


arr = [1,2,3]
arr.append(4)
print(arr)


# insert


arr = [1,2,4]
arr.insert(1, 100)

print(arr)


# erase(index se delete)


arr = [1,2,3,4]

del arr[1]

print(arr)


arr = [10,20,30,40]

del arr[3]

print(arr)


# pop back(last element delete)


arr = [1,2,3,4]

arr.pop()

print(arr)


arr = [10,20,30,40]

arr.pop(2)

print(arr)


# front(first element)


arr = [1,2,3,4]

print(arr[0])
print(arr[3])


#clear(all delete)


arr = [1,2,3,4]

arr.clear()
print(arr)
print(len(arr))
print(type(arr))
print(arr == [])



#empty(check empty)

arr = []

if not arr:
    print("empty")



# size(number of element)

arr = [1,2,3,4,5]

print(len(arr))



#capacity/max_size


arr = [1,2,3,4]

print(arr.__sizeof__())


