# sort character by frequency

class solution:
    def frequencySort(self, s):

        freq = [(0, chr(i + ord('a'))) for i in range(26)]

        for ch in s:
            index = ord(ch) - ord('a')

            freq[index] = (freq[index][0] + 1, ch)

            freq.sort(key=lambda x: (-x[0], x[1]))

            result = [ch for f, ch in freq if f > 0]

            return result
        

if __name__ == "__main__":
    sol = solution()
    s = "true"
    result = sol.frequencySort(s)
    print(result)


#maximum nesting depth of parenthesis


class solution:
    def maxDepth(self, s: str) -> int:

        p = 0
        ans = 0
        for ch in s:

            if ch == '(':
                p += 1

            elif ch == ')':
                p -= 1

            ans = max(ans, p)

        return ans
    
if __name__ == "__main__":
    sol = solution()
    s = "(1+(2*3)+((8)/4))+1"

    result = sol.maxDepth(s)

    print("max Depth:", result)


#roman numerals to integer


class solution:
    def romanToInt(self, s: str) -> int:

        roman = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

        res = 0

        for i in range(len(s) - 1):

            if roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]]

            else:
                res += roman[s[i]]

        return res +roman[s[-1]]
    
if __name__ == "__main__":
    sol = solution()

    s = "MCMXCIV"
    result = sol.romanToInt(s)

    print("integer value:", result)


#count number of substring


def at_most_k_distance(s, k):
    left, res = 0, 0
    freq = {}

    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1

        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:

                del freq[s[left]]
                left += 1

        res += (right - left + 1)
    return res

def count_substring(s, k):
    return at_most_k_distance(s, k) - at_most_k_distance(s, k - 1)

def main():
    s = "pqpqs"
    k = 2

    print("Count:", (s, k))


#sum of beauty of all substring


def beauty_sum(s):
    n = len(s)
    total = 0

    for i in range(n):
        freq = {}

        for j in range(i, n):
            freq[s[j]] = freq.get(s[j], 0) + 1

            values = freq.values()
            maxi = max(values)
            mini = min(values)

            total += (maxi - mini)

    return total

def main():
    s = "xyx"
    print("beauty sum:", beauty_sum(s))

if __name__ == "__main__":
    main()


#reverse words in a string

class solution:
    def reverseWords(self, s: str) -> str:

        words = []

        word = " "

        for ch in s:
            if ch != " ":
                word += ch

            elif word:
                words.append(word)
                word = ""

            words.reverse()

            return " ".join(words)
        
if __name__ == "__main__":
    obj = solution()
    s = " amazing coding skills"

    print(obj.reverseWords(s))

    