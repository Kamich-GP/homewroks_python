pol= ["level", "socet", "komok", "radar", "madam", "jordan", "kamol"]


def palindroms(words):
    palindroms = []

    for word in words:
        word1 = word[::-1]

        if word.lower() == word1.lower():
            palindroms.append(word)

    return palindroms


palindrome_words = palindroms(pol)

print("Палиндромы:")
for word in palindrome_words:
    print(word)