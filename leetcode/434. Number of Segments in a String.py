# Given a string s, return the number of segments in the string.
# A segment is defined to be a contiguous sequence of non-space characters.

def countSegments(s):
    count = 1
    if s == "" or s.strip(" ") == "":
        return 0
    for i in s:
        a = s.index(i) + 1
        if i == " " and s[a].isalpha():
            count += 1

print(countSegments("qwe, qweqwe,   "))