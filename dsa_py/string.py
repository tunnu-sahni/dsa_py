# #string = character of sequence (index 0 to start)
# #rule
# #1 it is the empty string"".
# #2 if A is a valid parentheses string, then so is" ("+A+")"
# #3 if A and B are valid parentheses string, then A+B is also valid


class solution:
    def removeOuterParentheses(self, s):
        result = ""

        level = 0

        for char in s:
            if char == '(':
                if level > 0:
                    result += char

            elif char == ')':
                level -+ 1
                if level > 0:
                    result += char
        return result
    
s = "(()())(())"
sol = solution()

print(sol.removeOuterParentheses(s))


# #reverse words in a string

# class solution:
#     def reverseWords(self, s: str) -> str:
#         words = []
#         word = ""
        
#         for ch in s:
#             if ch != " ":
#                 word += ch
            
#             elif word:
#                 words.append(word)

#                 word = " "

#         if word:
#             words.append(word)

#         words.reverse()

#         return " ".join(words)
    
# if __name__ == "__main__":
#     obj = solution()
#     s = " amazing coding skills "
#     print(obj.reverseWords(s))


# class solution:
#     def reverseWords(self, s: str) -> str:
#         result = " "

#         i = len(s) - 1

#         while i >= 0:

#             while i >= 0 and s[i] == " ":
#                 i -= 1
            
#             if i < 0:
#                 break

#             end = i

#             while i >= 0 and s[i] != " ":
#                 i -= 1

#                 word = s[i + 1:end + 1]

#                 if result != "":
#                     result += " "

#                 result += word

#             return result
        
# if __name__ == "__main__":
#     obj = solution()
#     s = " amazing coding skills "
#     print(obj.reverseWords(s))



# #largest odd number in a string


# class solution:
#     def largestOddNum(self, s: str) -> str:
#         ind = -1
#         i = 0

#         for i in range(len(s) - 1, -1, -1):

#             if (int(s[i]) % 2) == 1:
#                 ind = i
#                 break

#         i = 0
#         while i <= ind and s[i] == '0':
#             i += 1

#         return s[i:ind + 1]
    
# solution = solution()
# num = "504"
# result = solution.largestOddNum(num)

# print("Largest odd number:", result)


# #longest common prefix


# def longest_common_prefix(strs):
#     if not strs:
#         return " "
    
#     for i in range(len(str[0])):
#         ch = strs[0][i]

#         for word in strs:
#             if i >= len(word) or word[i] != ch:
#                 return strs[0][:i]
            
#     return strs[0]

# print(longest_common_prefix(["flower", "flow", "flight"]))



#isomorphic string


# class solutioin:
#     def isomorphicString(self, s, t):

#         m1, m2 = [0] * 256, [0] * 256

#         n = len(s)

#         for i in range(n):
#             if m1[ord(s[i])] != m2[ord(t[i])]:

#                 return False
            
#             m1[ord(s[i])] = i + 1
#             m2[ord(t[i])] = i + 1

#         return True
    
# if __name__ == "__main__":
#     solution()

#     s = "paper"
#     t = "tittle"

#     if solution.isormophicString(s, t):
#         print("String are isomorphic.")

#     else:
#         print("String are not isomorphic.")



#check if one string is rotation of another


class solution:
    def rotateString(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False
        
        for i in range(len(s)):
            rotated = s[i:] + s[:i]

            if rotated == goal:
                return True
            
        return False
    
sol = solution()

print(sol.rotateString("rotation", "tionrota"))


class solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        doubled_s = s + s

        return goal in doubled_s
    
sol = solution()

print(sol.rotateString("rotation", "tionrota"))



#check if two string are anagrams of each other


def CheckAnagrams(str1, str2):

    if len(str1) != len(str2):
        return False
    
    if sorted(str1) == sorted(str2):
        return True
    
    return False

if __name__ == "__main__":

    str1 = "INTEGER"
    str2 = "TEGERNI"

    if CheckAnagrams(str1, str2):
        print("True")

    else:
        print("Flase")


def CheckAnagrams(str1, str2):

    if len(str1) != len(str2):
        return False
    
    freq = [0] * 26

    for char in str1:
        freq[ord(char) - ord('A')] += 1

    for char in str2:
        freq[ord(char) - ord('A')] -= 1

    for count in freq:
        if count != 0:
            return False
        
    return True

if __name__ == "__main__":
    str1 = "INTEGER"
    str2 = "TEGERNI"

    if CheckAnagrams(str1, str2):
        print("True")

    else:
        print("False")