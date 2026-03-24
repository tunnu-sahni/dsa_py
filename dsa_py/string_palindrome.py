# check if the given string is palindrome or not

class solution:
    def is_palindrome(s):
        left, right = 0, len(s) - 1

        while left < right:
            if not s[right]. isalnum():
                left += 1
            elif  s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True
if __name__ == "__main__":
    str = "ABCDCBA"
    ans = is_palindrome(str)

    if ans:
        print("palindrome")

    else:
        print("Not palindrome")


def palindrome(i, s):
    if i >= len(s) // 2:
        return True
    if s[i] != s[len(s) - i - 1]:
        return False
    

if __name__ == "__main__":
    s = "madam"
    print(palindrome(0, s))