# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.
def isAnagram(s, t):
    for i in s:
        if s.count(i) == t.count(i):
            continue
        else:
            return False
    for i in t:
        if s.count(i) == t.count(i):
            continue
        else:
            return False
    return True