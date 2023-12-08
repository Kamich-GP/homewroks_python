# Given an array of strings words, return the words that can be typed using letters of the
# alphabet on only one row of American keyboard like the image below.
# In the American keyboard:
# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".
def findWords(words):
    first = "qwertyuiop"
    second = "asdfghjkl"
    third = "zxcvbnm"
    returnlist = []
    check1 = ""
    check2 = ""
    check3 = ""
    for a in words:
        for b in a:
            if b.lower() in first:
                check1 += b
            elif b.lower in second:
                check2 += b
            elif b.lower in third:
                check3 += b
        if check1 == a or check2 == a or check3 == a:
            returnlist.append(a)
            check1 = ""
            check2 = ""
            check3 = ""
        else:
            check1 = ""
            check2 = ""
            check3 = ""
    return returnlist


