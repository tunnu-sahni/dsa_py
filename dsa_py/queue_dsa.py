from collections import deque

q = deque()


d = [10,20,30]

q = deque()


#enqueue(push/add)


q = [10,20,30,40,50]

q.append(10)
print(q) 
print(10)
print(40)


#dequeue(remove)


q = [1,2,3,4,5,6]

print(q.pop())
print(q.pop())


d = [10,20,304,57,67]

print(d.pop(2))
print(d.pop(3))


#front(first element)


d = [10,20,30,40]

print(d[0])
print(d[2])


#rear(last element)


q = [1,2,3,4,5]

print(q[-1])
print(q[1])
print(q[2])


#size

s = [1,2,3,4,5,6]

print(len(s))
print(len(s))



#empty check


s = [1,2,3,4,5]

if not q:
    print("queue is empty")


print(q.clear())


#traversal

s = [1,2,3,4,5,6,6]

for s in q:
    print(s)