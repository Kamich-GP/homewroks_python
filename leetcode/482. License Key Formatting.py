# You are given a license key represented as a string s that consists of only alphanumeric characters and dashes.
# The string is separated into n + 1 groups by n dashes. You are also given an integer k.
# We want to reformat the string s such that each group contains exactly k characters, except for the first group,
# which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash
# inserted between two groups, and you should convert all lowercase letters to uppercase.
# Return the reformatted license key.
def licenseKeyFormatting(s, k):
    s = s.reverse()
    count = 0
    clearstring = s.replace("-", "")
    newstring = ""
    for i in clearstring:
        count += 1
        newstring += i.upper()
        if count == k:
            newstring += "-"
            count -= k
    if clearstring == "":
        return ""
    elif newstring[-1] == "-":
        newstring = newstring[:-1]
    return newstring[::-1]

