d = {}

d["apple"] = 10
d["banana"] = 20

print(d["apple"])
print(d["banana"])


#hashing function


s = {}

s["mango"] = 5
s["the quick brown fox jumps over the lazy dog"] = 50

print(hash("mango"))
print(hash("the quick brown fox jumps over the lazy dog"))


# hash table 

table = [[] for _ in range(5)]

def insert(key):
    index = key % 5
    table[index]. append(key)

insert(10)
insert(15)

print(table)


# set(hashing use)

s = {1,2,3}
print(2 in s)
print(4 in s)


#frequency count

arr = [1,2,2,3,3,3]

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

print(freq)