#create dictionary

student = {
    "name ": "tunnu sahni",
    "age ": 20
}

print(student)


student = {
    "name": "adarsh kumar",
    "age": 21
}

print(student)


employee = {
    "name": "john, doe",
    "age": 30
}

print(employee)


#map function
#access value

student = {
    "name": "tunnu",
    "age": 20

}

print(student["name"])


customer = {
    "name": "raja",
    "age": 25
}

print(customer["name"])


#insert/update


student["city"] = "delhi"
student["age"] = 21

print(student)


student["capital"] = "new delhi"
student["age"] = 32

print(student)



#delete

del student["age"]
print(student)


del customer["age"]
print(customer)


#pop


student = ["name", "age", "city"]
age = 32
name = "tunnu"
city = "delhi"
print(student)
student.pop(1)


#size

print(len(student))



arr = [1,2,2,3,3,3]

freq ={}
for num in arr:
    freq[num] = freq.get(num, 0) + 1
print(freq)



arr = [10,20,30,40,50]

freq = {}
for num in arr:
    freq[num] = freq.get(num, 1) + 1
    print(freq)


#first non repeating element


arr = [1,2,2,3,3,4]

freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1

for num in arr:
    if freq[num] == 1:
        print(num)
        break


#two sum probleem


nums = [2,7,11,15]
target = 9

d = {}
for i in range(len(nums)):
    diff = target - nums[i]
    if diff in d:
        print(d[diff], i)
        break
    d[nums[i]] = i