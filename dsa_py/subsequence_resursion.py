#generate all binary strings

# def generate(n, curr, result):

#     if len(curr) == n:
#         result.append(curr)
#         return
    
#     generate(n, curr + "0", result)

#     if not curr or curr[-1] != '1':
#         generate(n, curr + "1", result)

# def main():
#     n = 3
#     n = 2
#     result = []

#     generate(n, "", result)

#     print(result)

# if __name__ == "__main__":
#     main()


# #generate paranthesis

# def is_valid(s):
#     balance = 0
#     for c in s:
#         if c == '(':
#             balance += 1

#         else:
#             balance -= 1
#         if balance < 0:
#             return False
#     return balance == 0

# def generate_all(curr, n, res):
#     if len(curr) == 2 * n:
#         if is_valid(curr):
#             res.append(curr)
#         return 
    
#     generate_all(curr + '(', n, res)
#     generate_all(curr + ')', n, res)

# def generate_parenthesis(n):
#     res = []
#     generate_all("", n, res)
#     return res

# def main():
#     result = generate_parenthesis(3)
#     for s in result:
#         print(s)

# if __name__ == "__main__":
#     main()


# def backtrack(curr, open, close, n, res):
#     if len(curr) == 2 * n:
#         res.append(curr)
#         return 
    
#     if open < n:
#         backtrack(curr + '(', open + 1, close, n, res)

# def generate_parenthesis(n):
#     res = []
#     backtrack("", 0, 0, n, res)
#     return res

# def main():
#     result = generate_parenthesis(3)
#     for s in result:
#         print(s)

# if __name__ == "__main__":
#     main()


#power set


class solution:
    def getSubsequences(self, s: str) -> list[str]:
        n = len(s)
        total = 1 << n

        subsequences = []

        for mask in range(total):
            subseq = []

            for i in range(n):

                if mask & (1 << i):
                    subseq.append(s[i])

                subsequences.append("".join(subseq))
                return subsequences
            
if __name__ == "__main__":
    s = "abc"

    sol = solution()

    subsequences = sol.getSubsequences(s)

    for subseq in subsequences:
        print(f'" {subseq}"')


#combination sum

# class solution:
#     def findCombination(self, ind, target, arr, ans, ds):
#         pass

#         if ind == len(arr):
#             if target == 0:
#                 ans.append(list(ds))

#             return
        
#         if arr[ind] <= target:
#             ds.append(arr[ind])

#             self.findCombiantion(ind, target - arr[ind], arr, ans, ds)

#             ds.pop()

#             self.findCombinationSum(self, target)
#             ans = []
#             ds = []

#             self.findCombination(0, target, ans, ds)
#             return ans
        
# if __name__ == "__main__":
#     obj = solution()
#     v = [2, 3, 6, 7]
#     target = 7

#     ans = obj.combinationSum(v, target)

#     print("combination are: ")
#     for combination in ans:
#         print(" ".join(map(str, combination)))
        


#letter combination of the phone number


# class solution:
#     def __init__(self):
#         self.map = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

#         def helper(self, digits, ans, index, current):

#             if index == len(digits):
#                 ans.append(current)
#                 return
#             s = self.map[int(digits[index])]

#             for char in s:
#                 self.helper(digits, ans, index + 1, current + char)

#                 def letterCombinations(self, digits):

#                     ans = []

#                     if not digits:
#                         return ans
                    
#                     self.helper(digits, ans, 0, "")
#                     return ans
                
# if __name__ == "__main__":
#     sol = solution()
#     digits = "23"
#     result = sol.letterCombinations(digits)

#     print(result)