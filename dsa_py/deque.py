#create deque


from collections import deque

dq = deque()


#insert operation


# dq.append(10)
# dq.appendleft(5)

# print(dq)

# dq.append(100)
# dq.appendleft(25)

# print(dq)


#delete operation


# from collections import deque

# dq = deque([1, 2, 3])

# print(dq.pop())      # 3
# print(dq.popleft())  # 1
# print(dq)            # deque([2])



#access elements


# dq = deque([10,20,30,40])

# print(dq[0])
# print(dq[-1])
# print(dq[1])


# dq = deque([1,2,3,4,5,6,7,8,9,10])

# print(dq[3])
# print(dq[6])
# print(dq[0])


#other important functions


# dq.extend([1,2,3])

# print(dq)
# print(dq[1])

# dq.extend([10,20,30,40,50,60])

# print(dq[3])
# print(dq[-1])
# print([0])


# #extendleft

# dq.extendleft([4,5])

# print(dq[3])


#rotate

dq = deque([1,2,3,4])

dq.rotate(1)

dq.rotate(-1)

print(dq)

#clear

dq = deque([1,2,3])

print(dq.clear())

#count

dq = deque([1,2,3,4,5,6,7])

print(dq.count(2))

print(dq.count(1))


