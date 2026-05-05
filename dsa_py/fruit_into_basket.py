#fruit into baskets

class solution:
    def totalFruit(self, fruits):
        max_fruits = 0
        for start in range(len(fruits)):
            basket = {}

            current_count = 0

            for end in range(start, len(fruits)):
                basket[fruits[end]] = basket.get(fruits[end], 0) + 1

                if len(basket) > 2:
                    break

                current_count += 1

            max_fruits = max(max_fruits, current_count)

        return max_fruits
    
if __name__ == "__main__":
    obj = solution()
    fruits = [1, 2, 1]
    print(obj.totalFruit(fruits))
#tm = O(n2)
#sc = O(1)

from collections import defaultdict

class solution:
    def totalFruit(self, fruits):
        basket =defaultdict(int)

        left = 0
        max_fruits = 0

        for right in range(len(fruits)):
            basket[fruits[right]] += 1

            while len(basket) > 2:
                basket[fruits[left]] -= 1

                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                    left += 1

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits
    
if __name__ == "__main__":
    obj = solution()
    fruits = [1, 2, 1, 2, 3]
    print(obj.totalFruit(fruits))


class solution:
    def totalFruit(self, fruits):
        maxlen = 0
        lastfruits = secondlastfrruit = - 1
        currcount = 0
        lastfruitstrak = 0
        for fruit in fruits:
            if fruit == lastfruits or fruit == secondlastfrruit:
                currcount += 1

            else:
                currcount = lastfruits + 1
                if fruit == lastfruits:
                    lastfruits += 1
                else:
                    lastfruits_streak = 1
                    secondlastfrruit = lastfruits
                    lastfruits = fruit
                    maxlen = max(maxlen, currcount)
            return maxlen
if __name__ == "__main__":
    sol = solution()
    fruits = [ 1, 2, 1, 2, 3]
    print(sol.totalFruit(fruits))
