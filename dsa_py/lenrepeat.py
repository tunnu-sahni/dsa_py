#length longest substring without any repeating character

class solution:
    def longestRepeatingSubstring(self, s):
        n = len(s)
        maxlen = 0

        """" Iterate through all possible starting points of the substring"""

        for i in range(n):
            """" Hash to track characters the current substring window"""
            hash_set = [0] * 256
            for j in range(i, n):
                """" If s[j] is already in the current substring window """

                if hash_set[ord(s[j])] == 1:
                    break
                """ Update the hash_set to mark s[j] as present in the current window """
                hash_set[ord(s[j])] = 1

                """ Calculate the length of the current substring """

                current_len = j - i + 1

                """ Update maxlen if the current substring length is greater """
                maxlen = max(maxlen, current_len)

            return maxlen
        
if __name__ == "__main__":
    input_str = "cadbzabcd"
    sol = solution()

    length = sol.longestRepeatingSubstring(input_str)

    print("Length of longest substring window repeating character: ", length)
#TM = O(N^2)
#SC = O(1)

class solution:
    """Function to find longest substring without repeating characters """

    def longestNonRepeatingSubstring(self, s):
        n = len(s)
        HashLen = 256
        """ Hash table to store last occurence of each character """

        hash = [-1] * HashLen
        """ Initialize hash table with -1 (indicating no occurence) """

        for i in range(HashLen):
            hash[i] = -1
            l, r, maxLen = 0, 0, 0
            while r < n:
                """ If current character s[r] is already in the substring """

                if hash[ord(s[r])] != -1:
                    """ Move left pointer to the right of the last occurence of s[r] """
                    l = max(hash[ord(s[r])] + 1, l)
                    current_len = r - l + 1
                    maxLen = max(current_len, maxLen)

                    """ Store the index of the current character in the hash table """
                    hash[ord(s[r])] = r
                    r += 1

                return maxLen
            
if __name__ == "__main__":
    s = "cadbzabcd"
    sol = solution()

    result = sol.longestNonRepeatingSubstring(s)
    print("The maximum length is: ")
    print(result)

#TM = O(N)
#SC = O(1)