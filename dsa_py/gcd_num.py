def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solution():
    print(gcd(12, 18))

solution()


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(12, 18))
print(gcd(6, 12))