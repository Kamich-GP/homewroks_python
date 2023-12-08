# Write a function that takes the binary representation of an unsigned
# integer and returns the number of '1' bits it has (also known as the Hamming weight).
def hammingWeight(n):
    return str(n).count("1")
n = 11111111111111111111111111111101
print(hammingWeight(n))