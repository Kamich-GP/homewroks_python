# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing
# all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
def isPalindrome(s):
    a = ""
    for i in s:
        if i.isalpha() or i.isalnum():
            a += i
    if a.lower() == a[::-1].lower():
        return True
    else:
        return False

print(isPalindrome("a, b : a"))