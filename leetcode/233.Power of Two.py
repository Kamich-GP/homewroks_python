# Given an integer n, return true if it is a power of two. Otherwise, return false.
#
# An integer n is a power of two, if there exists an integer x such that n == 2x.
def isPowerOfTwo(n):
    values = [2**i for i in range(0, 100)]
    if n in values:
        return True
    else:
        return False
print(isPowerOfTwo(16))