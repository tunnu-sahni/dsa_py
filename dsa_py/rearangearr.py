#rearrange array element by sign

# def rearrange(arr):
#     pos = []
#     neg = []

#     for num in arr:
#         if num >= 0:
#             pos.append(num)
            

#         else:
#             neg.append(num)

#     i = j = k = 0
#     result = []

#     while i < len(pos) and j < len(neg):
#         result.append(pos[i])
#         result.append(neg[j])

#         i += 1
#         j += 1

#     while i < len(pos):
#         result.append(pos[i])
#         i += 1

#     while j < len(neg):
#         result.append(neg[j])

#     return result

# arr = [1, -2, 3, -4, -1, 4]

# print(rearrange(arr))


# def rearrange(arr):
#     n = len(arr)
#     result = [0] * n

#     pos_index = 0
#     neg_index = 1

#     for num in arr:
#         if num >= 0:
#             result[pos_index] = num
#             pos_index += 2

#         else:
#             result[neg_index] = num
#             neg_index += 2

#     return result

# arr = [1, -2, 3, -4]
# print(rearrange(arr))


