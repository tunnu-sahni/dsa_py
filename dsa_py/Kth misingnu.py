#kth missing positive number

class MissingKFinder:
    def missing_k(self, vec, k):
        for num in vec:
            if num <= k:
                k += 1
            else:
                break
        return k
    

vec = [4, 7, 9, 10]
k = 4

finder = MissingKFinder()
ans = finder.missing_k(vec, k)

print("the missing number is:", ans)



class MIssingKFinder:
    def missng_k(self, vec, k):
        low, high = 0, len(vec) - 1

        while low <= high:
            mid = (low + high) // 2

            missing = vec[mid] - (mid + 1)

            if missing < k:
                low = mid + 1

            else:
                high = mid - 1

vec = [4, 7, 9, 10]
k = 4
k = 5

finder = MissingKFinder()
ans = finder.missing_k(vec, k)

print("the missing number is:", ans)
