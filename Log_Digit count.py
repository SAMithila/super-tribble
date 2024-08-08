import math

def count_logarithm(n):
    if n == 0:
        return 1
    return math.floor(math.log10(n)) + 1

n = 12345
print(count_logarithm(n))