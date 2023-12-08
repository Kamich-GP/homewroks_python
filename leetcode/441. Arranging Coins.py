# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows
# where the ith row has exactly i coins. The last row of the staircase may be incomplete.
# Given the integer n, return the number of complete rows of the staircase you will build.

def arrangeCoins(n):
    forreturn = 0
    count = 0
    while True:
        count += forreturn + 1
        if n == 1:
            return 1
        elif n == 0:
            return 0
        elif count > n:
            return forreturn
        elif count == n:
            return forreturn + 1
        elif count <= n:
            forreturn += 1