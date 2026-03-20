#dictionary of list

# mp = {}

# mp[1] = ["A", "B"]
# mp[2] = ["C"]

# print(mp)

# from collections import defaultdict

# mp = defaultdict(list)

# mp[1].append("A")
# mp[1].append("B")
# mp[2].append("C")

# print(mp)


# #functions equivalent
# #insert


# mp[1].append("A")
# mp[1].append("B")

# print(mp)
# mp[1].append("C")


# #find


# if 1 in mp:
#     print(mp[1])


# #iteration


# for key, values in mp.items():
#     print(key, values)

# for key, values in mp.items():
#     for value in values:
#         print(key, value)


# mp.clear()


# for val in mp[1]:
#     print(val)


# #group elements

# arr = ["apple", "ant", "bat", "ball", "cat"]

# mp = defaultdict(list)

# for word in arr:
#     key = word[0]
#     mp[key].append(word)

# print(mp)


# #group anagrams

# from collections import defaultdict

# words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# mp = defaultdict(list)

# for w in words:
#     key = "".join(sorted(w))
#     mp[key].append(w)

#     print(mp.values())


#multiple values per key


from collections import defaultdict


students = {
    ("math", "tunnu"),
    ("math", "munnu"),
    ("english", "sahni")
}

mp = defaultdict(list)

for sub, name in students:
    mp[sub].append(name)

print(mp)