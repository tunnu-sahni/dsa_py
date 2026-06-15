# minimum multiplication to reach end

from collections import deque

class solution:
    def minimumMultiplications(self, arr, start, end):
        """
        finds the minimum number of multiplications to transform start into end
        using elements from arr under modulo 100000.
        """
        # queue to store (numbr , steps) pairs for BFS
        q = deque()
        q.append((start, 0))

        dist = [int(1e9)] * 100000
        dist[start] = 0
        mod = 100000

        while q:
            node, steps = q.popleft()

            # try multiplying node with each elements in arr
            for factor in arr:
                num = (factor * node) % mod

                if steps + 1 < dist[num]:
                    dist[num] = steps + 1

                    if num == end:
                        return steps + 1
                    q.append((num, steps + 1))

            return -1
        
if __name__ == "__main__":
    start, end = 3, 30
    arr = [2, 5, 7]
    obj = solution()
    ans = obj.minimumMultiplications(arr, start, end)
    print(ans)