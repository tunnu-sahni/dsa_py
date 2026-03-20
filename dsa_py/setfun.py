# set

# s = {1,2,3,4}

# print(s)

# s = {10,20,30,40}
# print(s)

# x = {1,2,2,3,4,5,6,6}
# print(x)

# #add(insert element)

# s = {1,2,3,4}
# s.add(5)
# print(s)
# s.add(9)
# print(s)



# # update(multiple element add)


# s = {1,2,3}
# s.update([4,5])
# print(s)
# s.update([5,6])
# print(s)


# #remove

# x = {1,2,3}
# x.remove(2)
# print(x)
# x.remove(1)
# print(x)


# #remove 

# s = {1,2,3}
# s.remove(2)
# print(s)


# # discard

# s = {1,2,3}
# s.discard(2)
# print(s)
# print(s.discard(1))


# #pop(random number delete)


# set = {1,2,3,4,5}
# set.pop()
# print(set)


# set = {1,2,3,4}
# set.clear()
# print(set)



# s = {1,2,3}
# print(len(s))
# print(s)
# print(3 in s)
# print(5 in s)




# set = {10,20,30,40}
# if not set:
#     print("set is empty")
#     print("set")



# #find/search


# set = {1,2,3,4,5}

# if 2 in set:
#     print("2 is found in set")
# if 7 in set:
#     print("7 is found in set")


# #set operation


# a = {1,2,3}
# b = {3,4,5}

# print(a.union(b))


x = {10,20,30,40}
y = {50,60,70,80}

print(x | y)


a = {1,2,3,4}
b = {3,4,5,6}

print(a.intersection(b))

print(a & b)


#symmetric difference


a = {1,2,3,4}
b = (3,4,5,6)

print(a.symmetric_difference(b))


#remove duplicates


arr = [1,2,2,3,4,4]

unique = list(set(arr))
print(unique)


#check duplicates


arr = [10,20,30,40,50,60,60,60,70,70]

if len(arr) != len(set(arr)):
    print("duplicates present")
    print("duplicates found")



#fast lookup

s = {1,2,3,4,5}
print(3 in s)
print(10 in s)



#find common elements

a = [1,2,3,4,5]
b = [4,5,6,7,8]
print(set(a) & set(b))