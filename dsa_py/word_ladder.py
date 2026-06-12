from collections import deque

class Solution:
    # Function to calculate the shortest transformation sequence length
    def wordLadderLength(self, startWord, targetWord, wordList):
        q = deque([(startWord, 1)])
        st = set(wordList)
        if startWord in st:
            st.remove(startWord)

        while q:
            word, steps = q.popleft()

            # If target word is found
            if word == targetWord:
                return steps

            # Try changing every character
            for i in range(len(word)):
                original = word[i]
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + ch + word[i+1:]
                    if newWord in st:
                        st.remove(newWord)
                        q.append((newWord, steps + 1))
        return 0

if __name__ == "__main__":
    wordList = ["des", "der", "dfr", "dgt", "dfs"]
    startWord = "der"
    targetWord = "dfs"
    obj = Solution()
    print(obj.wordLadderLength(startWord, targetWord, wordList))


from collections import deque

class Solution:
    def findSequences(self, beginWord, endWord, wordList):
        """
        Finds all the shortest transformation sequences from beginWord to endWord.
        Each transformation changes one letter and must exist in wordList.
        """
        word_set = set(wordList)  # Fast lookup and deletion
        queue = deque([[beginWord]])  # Each element is a path (list of words)
        used_on_level = [beginWord]
        level = 0
        ans = []

        while queue:
            path = queue.popleft()

            # Remove used words when moving to the next BFS level
            if len(path) > level:
                level += 1
                for word in used_on_level:
                    word_set.discard(word)

            word = path[-1]

            # If we found the target word
            if word == endWord:
                if not ans:
                    ans.append(path[:])
                elif len(ans[0]) == len(path):
                    ans.append(path[:])

            # Try changing each character of the current word
            for i in range(len(word)):
                original = word[i]
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in word_set:
                        path.append(new_word)
                        queue.append(path[:])
                        used_on_level.append(new_word)
                        path.pop()
        
        return ans


# Driver code
if __name__ == "__main__":
    wordList = ["des", "der", "dfr", "dgt", "dfs"]
    startWord, targetWord = "der", "dfs"
    obj = Solution()
    ans = obj.findSequences(startWord, targetWord, wordList)

    if not ans:
        print(-1)
    else:
        ans.sort(key=lambda x: "".join(x))
        for sequence in ans:
            print(" ".join(sequence))