#length of the longest subarray with zero sum

# def solve(a: list[int]) -> int:
#     max_len = 0
#     sum_index = {}

#     s = 0

#     for i, val in enumerate(a):
#         s += val
#         if s == 0:
#             max_len = i + 1
        
#         elif s in sum_index:
#             max_len = max(max_len, i - sum_index[s])

#         else:
#             sum_index[s] = i
#     return max_len

# def main():
#     a = [9, -3, 3, -1, 6, -5]
#     print(solve(a))

# if __name__ == "__main__":
#     main()


def maxLen(A: list[int], n: int) -> int:
    mpp: dict[int, int] = {}
    maxi = 0
    s = 0

    for i in range(n):
        s += A[i]
        if s == 0:
            maxi = i + 1

        else:
            if s in mpp:
                maxi = max(maxi, i - mpp[s])
            else:
                mpp[s] = i

    return maxi

def main():
    A = [9, -3, 3, -1, 6, -5]
    n = len(A)

    print(maxLen(A, n))

if __name__ == "__main__":
    main()